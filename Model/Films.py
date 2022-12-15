import pandas as pd
from Data import Data
import requests
import json

class Films:
    def __init__(self):
        self.data = Data.get_instance()

    def get_list_film(self):
        return self.data.df_movies

    def get_infos(self, id):
        url = 'https://www.allocine.fr/_/autocomplete/' + self.data.df_movies.loc[self.data.df_movies['id'] == id, 'title'].values[0]
        body = requests.get(url)
        json_data = json.loads(body.text)
        thumbnail = json_data['results'][0]['data']['thumbnail']
        id = json_data['results'][0]['data']['id']
        url = "https://www.allocine.fr/film/fichefilm_gen_cfilm=" + str(id) + ".html"

        return thumbnail,url

    def get_preview(self, id):
        pass