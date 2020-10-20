import dota2api
import requests
import webbrowser

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.core.window import Window
from time import sleep
from threading import Thread


class MainScreen(Screen):

    def find_matches(self):
        self.ids['find'].disabled = True
        self.ids['find'].text = "Fetching hero data..."
        t1 = Thread(target=self.add_matches, daemon=True)
        t1.start()

    def add_matches(self):
        API_KEY = self.ids['api_key'].text
        ACCOUNT_ID = int(self.ids['account_id'].text)
        BASE_TIMEOUT = 1
        NUMBER_OF_MATCHES = int(self.ids['number_of_matches'].text)
        api = dota2api.Initialise(API_KEY)
        hero_data = requests.get("https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key={}".format(API_KEY)).json()
        if hero_data['result']['status'] == 200:
            total_matches = 0
            matches = []
            self.ids['progress'].max = hero_data['result']['count']
            i = 0
            for hero in hero_data['result']['heroes']:
                self.ids['find'].text = "Queuing matches of {}: {}/{}".format(hero['name'].replace("npc_dota_hero_", ""), i+1, hero_data['result']['count'])
                hero_matches = []
                for match in api.get_match_history(matches_requested=NUMBER_OF_MATCHES, account_id=ACCOUNT_ID, hero_id=hero['id'])['matches']:
                    hero_matches.append(match["match_id"])
                    total_matches += 1
                sleep(BASE_TIMEOUT)
                i += 1
                self.ids['progress'].value = i
                matches.append(hero_matches)
            self.ids['progress'].value = 1
            self.ids['progress'].max = total_matches
            print(total_matches)
            self.loop_matches(matches, ACCOUNT_ID)
        else:
            self.ids['find'].text = "Server Error"

    def loop_matches(self, recent_matches, ACCOUNT_ID):
        for hero_matches in recent_matches:
            parse = True
            for match in hero_matches:
                print(match)
                self.ids['progress'].value += 1
                self.ids['find'].text = "Scanning match (hero{}): {}/{}".format(str(recent_matches.index(hero_matches)+1), str(int(self.ids['progress'].value)), self.ids['progress'].max)
                if not self.check_match(match, ACCOUNT_ID, parse):
                    parse = False
        self.ids['find'].text = "Done"


    def check_match(self, match, ACCOUNT_ID, parse):
        BASE_TIMEOUT = 1
        PARSE_TIMEOUT = 10
        BASE_API = "http://api.opendota.com/api/matches/"
        match_details = requests.get(BASE_API + str(match)).json()
        if parse == True:
            if match_details['version'] is None:
                self.ids['find'].text = "Requesting parse of match ({}): {}/{}".format(self.ids['find'].text.split("(")[1].split(")")[0], self.ids['find'].text.split(" ")[-1].split("/")[0], self.ids['find'].text.split(" ")[-1].split("/")[1])
                try:
                    if requests.get(match_details['replay_url']).status_code == 200:
                        requests.post("https://api.opendota.com/api/request/" + str(match))
                        while match_details['version'] is None:
                            self.ids['find'].text = "Parsing match ({}): {}/{}".format(self.ids['find'].text.split("(")[1].split(")")[0], self.ids['find'].text.split(" ")[-1].split("/")[0], self.ids['find'].text.split(" ")[-1].split("/")[1])
                            sleep(PARSE_TIMEOUT)
                            match_details = requests.get(BASE_API + str(match)).json()
                    else:
                        self.ids['find'].text = "Replay not available, skipping parsing"
                        sleep(BASE_TIMEOUT)
                        return False
                except Exception as e:
                    print(e)
        if match_details['version'] is not None:
            for player in match_details['players']:
                if player["account_id"] == ACCOUNT_ID:
                    if player['multi_kills'] is not None and '5' in player['multi_kills'].keys():
                        link_btn = Button(text="http://www.opendota.com/matches/" + str(match))
                        link_btn.bind(on_release=lambda touch: webbrowser.open(link_btn.text))
                        self.ids['links'].add_widget(link_btn)
                        break
            sleep(BASE_TIMEOUT)
        return True


class WindowManager(ScreenManager):
    pass


class Dota2_Rampage_Finder(App):

    def build(self):
        Window.size = (950, 600)
        return Builder.load_file("styling.kv")


Dota2_Rampage_Finder().run()
