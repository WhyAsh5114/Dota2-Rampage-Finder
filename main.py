import dota2api
import requests

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from time import sleep
from threading import Thread


class MainScreen(Screen):

    def find_matches(self):
        ACCOUNT_ID = int(self.ids['account_id'].text)
        NUMBER_OF_MATCHES = int(self.ids['number_of_matches'].text)
        API_KEY = self.ids['api_key'].text
        api = dota2api.Initialise(API_KEY)
        recent_matches = []
        for match in api.get_match_history(matches_requested=NUMBER_OF_MATCHES, account_id=ACCOUNT_ID)['matches']:
            recent_matches.append(match["match_id"])
        self.ids['progress'].max = len(recent_matches)
        self.ids['main'].remove_widget(self.ids['find'])
        t1 = Thread(target=self.loop_matches, daemon=True, args=(recent_matches, ACCOUNT_ID))
        t1.start()


    def loop_matches(self, recent_matches, ACCOUNT_ID):
        for match in recent_matches:
            self.check_match(match, ACCOUNT_ID)
            self.ids['progress'].value += 1


    def check_match(self, match, ACCOUNT_ID):
        BASE_API = "https://api.opendota.com/api/matches/"
        BASE_TIMEOUT = 0.5
        match_data_url = BASE_API + str(match)
        response = requests.get(match_data_url)
        match_details = response.json()
        for player in match_details['players']:
            if player["account_id"] == ACCOUNT_ID:
                if player['multi_kills'] is not None and '5' in player['multi_kills']:
                    self.ids['links'].add_widget(Label(text="http://www.opendota.com/matches/" + str(match)))
                    break
        sleep(BASE_TIMEOUT)


class WindowManager(ScreenManager):
    pass


class Dota2_Rampage_Finder(App):

    def build(self):
        return Builder.load_file("styling.kv")


Dota2_Rampage_Finder().run()
