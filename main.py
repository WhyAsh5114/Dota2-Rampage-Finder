import dota2api
import requests
from time import sleep

BASE_API = "https://api.opendota.com/api/matches/"
BASE_TIMEOUT = 1
MY_ACCOUNT_ID = int(input("Enter account id: "))
NUMBER_OF_MATCHES = int(input("Enter number of matches to record: "))
API_KEY = int(input("Enter API key: "))

api = dota2api.Initialise(API_KEY)

recent_matches = []
for match in api.get_match_history(matches_requested=100, account_id=MY_ACCOUNT_ID)['matches']:
    recent_matches.append(match["match_id"])


for match in recent_matches:
    response = requests.get(BASE_API + str(match))
    match_details = response.json()

    for player in match_details['players']:
        if 'personaname' in player.keys():
            if player["account_id"] == MY_ACCOUNT_ID:
                try:
                    if player['multi_kills'] is not None and '5' in player['multi_kills']:
                        print(player['multi_kills'])
                        print('We got a rampage: http://www.opendota.com/matches/%s' % match_details['match_id'])
                        break
                except Exception as e:
                    print(e)
    print("Not {}".format(match))
    sleep(BASE_TIMEOUT)
