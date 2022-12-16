import pandas as pd
from Data import Data
import requests
import json
import re
class Films:
    def __init__(self):
        self.data = Data.get_instance()

    def get_list_film(self):
        return self.data.df_movies

    def get_infos(self, id):
        try:
            url = 'https://www.allocine.fr/_/autocomplete/' + self.data.df_movies.loc[self.data.df_movies['id'] == id, 'title'].values[0]
            body = requests.get(url)
            json_data = json.loads(body.text)
            thumbnail = json_data['results'][0]['data']['thumbnail']
            id = json_data['results'][0]['data']['id']
            url = "https://www.allocine.fr/film/fichefilm_gen_cfilm=" + str(id) + ".html"
            id_video = json_data['results'][0]['data']['default_video']
            return thumbnail,url, id_video
        except:
            return "", "https://www.allocine.fr/", ""

    def get_preview(self, id, id_video):
        url = "https://www.allocine.fr/video/player_gen_cmedia=" + str(id_video) + "&cfilm=" + str(id) + ".html"
        print(url)
        body = requests.get(url)
        result = re.findall('''(?<=\<figure class=\"player player-auto-play js-player\" data-model=\")(.*)(?=data-player-dm-id)''', body.text)
        if result == []:
            return ""
        result = result[0].replace('\"', '')
        result = result.replace('&quot', '')
        result = result.replace(';', '')
        result = result.replace(':', '_')
        try:
            result = re.findall('''(?<=_).*?(?=,)''', result)[1]
        except:
            return ""

        url = "https://www.dailymotion.com/player/metadata/video/" + result
        body = requests.get(url)
        json_data = json.loads(body.text)
        return json_data['qualities']['auto'][0]['url']

