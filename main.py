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
        '''API_KEY = self.ids['api_key'].text
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
            self.ids['find'].text = "Server Error"'''
        recent_matches = [[5661801142, 5660391636, 5649248234, 5640982007, 5640932305, 5635781774, 5635475207, 5634397564, 5634325043, 5631228725, 5625512088, 5625477038, 5622913659, 5621132172, 5621089670, 5619545204, 5618323537, 5618220747, 5615565724, 5615502971, 5612989795, 5612633252, 5612580407, 5610859976, 5609353623, 5608069829, 5607894959, 5606644041, 5605201572, 5603799465, 5600650125, 5599099141, 5597749987, 5597284440, 5597122013, 5596372774, 5594995521, 5588353670, 5585313249, 5584430305, 5584080295, 5582552998, 5581077248, 5580987734, 5577844329, 5577719583, 5577673058, 5576374122, 5574998994, 5574878921, 5574788267, 5571441644, 5570530043, 5569717220, 5569673806, 5569479741, 5569362282, 5568924908, 5568048988, 5568000351, 5567912464, 5567218102, 5566500982, 5566384233, 5561319884, 5561275105, 5561216946, 5558257873, 5548449185, 5540042355, 5538911858, 5536991199, 5536629984, 5534587844, 5532942636, 5532870767, 5531098554, 5529411589, 5529312432, 5527965765, 5527473863, 5525733171, 5523312628, 5521222097, 5517041636, 5516886499, 5516459099, 5516364161, 5510058480, 5508033022, 5506883276, 5506525035, 5502738887, 5501234571, 5500242016, 5497478163, 5497312846, 5496138282, 5495962416, 5494294563], [], [], [5480500684, 5458578692, 5235805635], [5607786038, 5492714836, 5125896651], [5663420857, 5663354489, 5661750201, 5660493503, 5647820468, 5640876042, 5638448837, 5636771874, 5634073441, 5632761297, 5622805636, 5621032642, 5618279276, 5618184281, 5618025870, 5615454966, 5513815472, 5500306596, 5488600478, 5487070415, 5464933977], [5509996127, 5506688379, 5237362206, 5236211417, 5131545345], [5647893564, 5632651875, 5631071686, 5629820114, 5615376573, 5610932853, 5606594969, 5599141585, 5598065233, 5597254400, 5590214974, 5585612325, 5574762792, 5567321046, 5562840904, 5561117646, 5550148043, 5549995137, 5539821473, 5534777745, 5531029388, 5530988130, 5527536147, 5521485728, 5521312445, 5501296944, 5499940682, 5498696159, 5498371746, 5492972415, 5463667268, 5403943496, 5270772858], [], [5512524365, 5491507925, 5480345819, 5243463212], [5607858165, 5546372258, 5542019851, 5541692275, 5531336476, 5530917201, 5462364026, 5393776620, 5380294067, 5248980197, 5245642242, 5244136561], [5536703001, 5535269247, 5518921364, 5460241100, 5375621908], [], [5573493650, 5247066829], [5521143502, 5380154436], [], [5660197138, 5649377112, 5647985192, 5647856634, 5646445380, 5643793210, 5643662961, 5641224876, 5641040094, 5534726628, 5446495000, 5367820694, 5243375634, 5242267888], [5601200499, 5566961913, 5532825112, 5529536757, 5529473215, 5525535127, 5516614586, 5505713442, 5505442574, 5501395483, 5483504596, 5479373400, 5477531877, 5476649744, 5474820773, 5248596798], [5518793048, 5518669271, 5514214512, 5464978513, 5458404821, 5454781777, 5454703220, 5242124823], [5663178325, 5660271846, 5643699111, 5634106462, 5631280909, 5511401313, 5481858622], [], [5451632737], [5520895335], [5637054714, 5624149703, 5618138163, 5593854793, 5567265363, 5506637593, 5476157431], [5615414041, 5566234655, 5562737335, 5494260615, 5480196714, 5477592053], [5619487405, 5568683703, 5557950760, 5531209023, 5498418278, 5483155661, 5449993970], [5521413746], [5460299611], [5608107154, 5608025444, 5602236222, 5597782760, 5597178492, 5595510411, 5591851547], [5635429331, 5628275471, 5567828959, 5470180291, 5467062217], [5504395238], [5236269640], [5483235832], [5573415110, 5534653126, 5513967262, 5513931744, 5488543667, 5468311585, 5468119062, 5405976945, 5403865257], [], [5496925391], [], [5650857809, 5646545154, 5645338890, 5643736553, 5642438639, 5596263560, 5585276575, 5577898251, 5576259238, 5570579293, 5567589558, 5564215248, 5561166765, 5558124848, 5546570645, 5494341405, 5398599447, 5367659267, 5365992617, 5271150822], [5501437178], [5649338208, 5634159222, 5619584437, 5616811769, 5609403767, 5607982157, 5607821798, 5599491114, 5596795293, 5596449078, 5591922908, 5591686308, 5585703805, 5554797270, 5553242151, 5507044339, 5470225002, 5409738260, 5260402185, 5258700814, 5256891347, 5247317000, 5247223117], [5529600885, 5516304764, 5496976095, 5494600734, 5492636925, 5491867905, 5491802449, 5470374117, 5470134279, 5468709123, 5385662580], [5503125243], [5614071648, 5590674962, 5590606950, 5588850149, 5588424961, 5585462701, 5585405113, 5585366851, 5584016615, 5579369961, 5571226888, 5570827537, 5567469924, 5567397991, 5566920051, 5566325236, 5561380075, 5557881650, 5510170636, 5493402845, 5492764397, 5491418391, 5484787761, 5483195832, 5479055266, 5461916039, 5458292671, 5449685804, 5446198530, 5443510339, 5413230603, 5403449808, 5398444569, 5396399057, 5395828105, 5393861025, 5389726421, 5366089776, 5335224206, 5248823076, 5235980478], [], [5559747357, 5556198362, 5555225930, 5554962234, 5554911424], [5460722569, 5450093101], [5636992508, 5636847123, 5595455875, 5595040762, 5487170099, 5455169963], [], [], [], [5505409488], [5504458752], [5458486880, 5400437718, 5247750738], [], [5569625543, 5523222399, 5461974344], [], [], [5572148441, 5382737437, 5380505887], [5486968567], [], [5504030748], [5615323865, 5611410756, 5584129240, 5567135014, 5556258277, 5550191024, 5539858064, 5532674416, 5529155630, 5525599327, 5524394013, 5524025810, 5523531891, 5521576923, 5512156113, 5505377414, 5451385276, 5387632916], [5561026216, 5482028976, 5481773857, 5481747014, 5481724543, 5481707513], [], [], [5649157481, 5617989496, 5616854249, 5603748610, 5603589822, 5602869802, 5602036303, 5601117716, 5575057769, 5531155237, 5527414674, 5525628614, 5523572345, 5514829524, 5510912293, 5510796251, 5481910606, 5474743392, 5466616497, 5443698849, 5389637013, 5387527758, 5381979816, 5380590715, 5380054459, 5131507900], [5582596984, 5512462980, 5512311346], [5471729480], [5567713300, 5520957411, 5514315763, 5513998074, 5501342728, 5474999589, 5465049134, 5367753139], [5554649746], [5509549816], [5548373939, 5514127710, 5512764323, 5508681174, 5508456892, 5495594862, 5485780483, 5481962440, 5473769433, 5473358372, 5472484877, 5463425573, 5462564589, 5460556254, 5460187386, 5456643714, 5446609681, 5412476639, 5408065131, 5399779656, 5227483259], [5584248012, 5577779243, 5243754084], [5501205714], [], [], [], [], [], [5532990355, 5480315070, 5465434333, 5247505543], [], [], [5647929924, 5602379073, 5590139491, 5585503684, 5574733782, 5550317543, 5508544887, 5489946656, 5484379272, 5412702955], [5572204993], [5611377249, 5481689248, 5481053661, 5479002516, 5476096919, 5474707639, 5391677377], [5587027344, 5523384409], [], [5573453004], [5490034961, 5489154854, 5487618835, 5487413079, 5487354033, 5485832384], [], [], [5602795012, 5569567138, 5566437414, 5565706203, 5562788665, 5558073350, 5554706536, 5549953309, 5522108063, 5516678771, 5506942164, 5505870741, 5503185252, 5466680642, 5465198154, 5465150929, 5385825097, 5225966104], [5594938031, 5593508825, 5593466566, 5592332738, 5574710418, 5559844235, 5463603511, 5457269373, 5405248919], [5649214308, 5614136201, 5597222634, 5596411862, 5589936618, 5586952816, 5585555709, 5583967206, 5574922553, 5574848735, 5571375599, 5570756006, 5570687519, 5570475115, 5569767380, 5569110925, 5569024107, 5568870747, 5568098314, 5514693452, 5512239886, 5411344474, 5407248417, 5399722670, 5384312029, 5371859672, 5340046788, 5281117182, 5260471257, 5258605921, 5251621516, 5250568755, 5248721537, 5248648784, 5247381265, 5245919296, 5243942131, 5243700554, 5243538952, 5242478425, 5242369657, 5242215529, 5242053269, 5237703284, 5226103243, 5226042606], [5550039154, 5491461985], [5602315003, 5579293563, 5566582296, 5566544219, 5513903901], [5247170777], [5638115756, 5571297731, 5518849094, 5509660560, 5447846841, 5412754587], [], [5540092287, 5516776391, 5468357522, 5401515668, 5379946889, 5378443126, 5114933836], [5474962773, 5454583023], [], [5521074091, 5485877778, 5473414130, 5471838234], [5509609110, 5391737850], [], [5634251011, 5632697218, 5629644033, 5629599069, 5629560169, 5625603395, 5624190262, 5540170102, 5538370707, 5536561543, 5512199730, 5472015541], [], [], [5480390132, 5391586137], [5600551327, 5516528925, 5493062413, 5490077946], [], [5481815103], [5453097907], [5628250361, 5529660877, 5494071828], [], [5550256597, 5538321862, 5529357196, 5510963289, 5445778097], [5649292504, 5646485401, 5600575820, 5513869847], [], [5492869780]]
        total = 0
        for a in recent_matches:
            for b in a:
                total += 1
        self.ids['progress'].max = total
        print(total)
        self.loop_matches(recent_matches, int(self.ids['account_id'].text))

    def loop_matches(self, recent_matches, ACCOUNT_ID):
        for hero_matches in recent_matches:
            parse = True
            for match in hero_matches:
                print(match)
                self.ids['progress'].value += 1
                self.ids['find'].text = "Scanning match (hero{}): {}/{}".format(str(recent_matches.index(hero_matches)+1), str(int(self.ids['progress'].value)), self.ids['progress'].max)
                sleep(1)
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
                self.ids['find'].text = "Requesting parse of match: {}".format(self.ids['find'].text.split(" ")[-1].split("/")[0])
                try:
                    if requests.get(match_details['replay_url']).status_code == 200:
                        requests.post("https://api.opendota.com/api/request/" + str(match))
                        while match_details['version'] is None:
                            self.ids['find'].text = "Parsing match: " + self.ids['find'].text.split(" ")[-1].split("/")[0]
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
