import dota2api
import requests
import d2api

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from time import sleep
from threading import Thread


class MainScreen(Screen):

    def find_matches(self):
        self.ids['find'].disabled = True
        t1 = Thread(target=self.add_matches, daemon=True)
        t1.start()

    def add_matches(self):
        API_KEY = self.ids['api_key'].text
        ACCOUNT_ID = int(self.ids['account_id'].text)
        BASE_TIMEOUT = 0.5
        NUMBER_OF_MATCHES = int(self.ids['number_of_matches'].text)
        api = dota2api.Initialise(API_KEY)
        recent_matches = []
        self.ids['progress'].max = 119
        for i in range(1, 120):
            for match in api.get_match_history(matches_requested=NUMBER_OF_MATCHES, account_id=ACCOUNT_ID, hero_id=i)['matches']:
                recent_matches.append(match["match_id"])
            self.ids['progress'].value = i
            self.ids['find'].text = "Finding... Hero number: " + str(i) + '/119'
            sleep(BASE_TIMEOUT)
        print(len(recent_matches))
        self.ids['progress'].value = 0
        self.ids['progress'].max = len(recent_matches)
        t2 = Thread(target=self.loop_matches, daemon=True, args=(recent_matches, ACCOUNT_ID))
        t2.start()

    def loop_matches(self, recent_matches, ACCOUNT_ID):
        for match in recent_matches:
            self.check_match(match, ACCOUNT_ID)
            self.ids['progress'].value += 1
            self.ids['find'].text = "Looking at match: " + self.ids['progress'].value + "/" + str(len(recent_matches))
        self.ids['find'].text = "Done"


    def check_match(self, match, ACCOUNT_ID):
        BASE_API = "https://api.opendota.com/api/matches/"
        BASE_TIMEOUT = 1
        match_data_url = BASE_API + str(match)
        response = requests.get(match_data_url)
        match_details = response.json()
        for player in match_details['players']:
            if player["account_id"] == ACCOUNT_ID:
                if player['multi_kills'] is not None and '5' in player['multi_kills']:
                    self.ids['links'].add_widget(TextInput(text="http://www.opendota.com/matches/" + str(match)))
                    break
        sleep(BASE_TIMEOUT)


class WindowManager(ScreenManager):
    pass


class Dota2_Rampage_Finder(App):

    def build(self):
        return Builder.load_file("styling.kv")


Dota2_Rampage_Finder().run()
