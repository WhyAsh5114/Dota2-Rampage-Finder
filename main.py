import requests
import webbrowser

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
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

        req_num = int(self.ids['number_of_matches'].text)
        NUMBER_OF_MATCHES = req_num if req_num < 100 else 100
        
        hero_data = requests.get("https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key={}".format(API_KEY)).json()
        matches = []
        self.ids['progress'].max = hero_data['result']['count']
        raw_matches = requests.get(f"https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?account_id={ACCOUNT_ID}&matches_requested={NUMBER_OF_MATCHES}&key={API_KEY}").json()['result']['matches']
        for match in raw_matches:
            matches.append(match["match_id"])

        self.ids['progress'].max = NUMBER_OF_MATCHES
        self.loop_matches(matches, ACCOUNT_ID, NUMBER_OF_MATCHES)


    def loop_matches(self, recent_matches, ACCOUNT_ID, number_of_matches):
        for i, match in enumerate(recent_matches, 1):
            self.ids['progress'].value = i
            self.ids['find'].text = f"Scanning match: {str(i)}/{number_of_matches}"
            self.check_match(match, ACCOUNT_ID, i, number_of_matches)
        self.ids['find'].text = "Done"


    def check_match(self, match, ACCOUNT_ID, i, number_of_matches):
        BASE_TIMEOUT = 1
        PARSE_TIMEOUT = 10
        BASE_API = "http://api.opendota.com/api/matches/"

        match_details = requests.get(BASE_API + str(match)).json()
        if match_details['version'] is None:
            self.ids['find'].text = f"Requesting parse of match: {i}/{number_of_matches}"
            try:
                requests.post(f"https://api.opendota.com/api/request/{str(match)}")
                wait = 0
                while match_details['version'] is None:
                    self.ids['find'].text = f"Parsing match: {i}/{number_of_matches}"
                    wait += PARSE_TIMEOUT
                    sleep(PARSE_TIMEOUT)
                    match_details = requests.get(BASE_API + str(match)).json()
                    if wait > 60:
                        self.ids['find'].text = "API Timeout, Trying next... (Maybe API call limit reached)"
                        sleep(2)
                        break
                if match_details['version'] is None:
                    self.ids['find'].text = "Replay not available, skipping parsing"
                    sleep(BASE_TIMEOUT)
                    return False
            except Exception as e:
                print(e)

        for player in match_details['players']:
            if player["account_id"] == ACCOUNT_ID:
                if player['multi_kills'] is not None and '5' in player['multi_kills'].keys():
                    Clock.schedule_once(lambda dt: self.add_link("http://www.opendota.com/matches/" + str(match)))
                    print(f"Rampage found in match: {match}")
        sleep(BASE_TIMEOUT)
        return True


    def add_link(self, txt):
        link_btn = Button(text=txt)
        link_btn.height = 10
        link_btn.bind(on_release=lambda touch: webbrowser.open(link_btn.text))
        self.ids['links'].add_widget(link_btn)


class WindowManager(ScreenManager):
    pass


class Dota2_Rampage_Finder(App):

    def build(self):
        Window.size = (950, 600)
        return Builder.load_file("styling.kv")


Dota2_Rampage_Finder().run()
