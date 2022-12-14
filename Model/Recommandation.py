import pandas as pd
import json
import numpy as np
from Data import Data
from Session import Session


def get_list_id(list_dict):
    list_id = []
    for item in list_dict:
        list_id.append(item['id'])
    return list_id

class Recommandation:
    def __init__(self):
        self.session = Session.get_instance().session
        self.data = Data.get_instance()

    def get_list(self):
        try:
            if self.session['genres'] is None:
                self.session['genres'] = []
        except:
            self.session['genres'] = []

        try:
            if self.session['acteurs'] is None:
                self.session['acteurs'] = []
        except:
            self.session['acteurs'] = []

        try:
            if self.session['films'] is None:
                self.session['films'] = []
        except:
            self.session['films'] = []

        list_genre = self.session['genres']
        list_films = self.session['films']
        list_acteur = self.session['acteurs']

        recommandation = self.data.df_movies.loc[:, ['id', 'title', 'genres', 'vote_average', 'popularity']]
        recommandation['score'] = 0
        #add 10 to score if the genre is in the list of genre
        for genre in list_genre:
            recommandation['score'] = np.where(recommandation['genres']
                                               .apply(lambda item: genre in get_list_id(item if len(item) > 0 else [])),
                                               recommandation['score'] + 10,
                                               recommandation['score'])

        #add 5 to score if the film is in the list of film
        list_genre_to_up = {}
        for film in list_films:
            for genre in recommandation.loc[recommandation['id'] == film, 'genres'].values[0]:
                list_genre_to_up[genre['id']] = list_genre_to_up.get(genre['id'], 0) + 1

        for id, coef in list_genre_to_up.items():
            recommandation['score'] = np.where(recommandation['genres']
                                               .apply(lambda item: id in get_list_id(item if len(item) > 0 else [])),
                                               recommandation['score'] + 2 * coef,
                                               recommandation['score'])

        #add 1 to score if the actor is in the list of actor
        for acteur in list_acteur:
            recommandation['score'] = np.where(self.data.df_credits['cast']
                                               .apply(lambda item: acteur in get_list_id(item if len(item) > 0 else [])),
                                               recommandation['score'] + 1,
                                               recommandation['score'])

        recommandation = recommandation.sort_values(by=['score', 'vote_average', 'popularity'], ascending=False)
        recommandation = recommandation.loc[~recommandation['id'].isin(list_films), :]
        return recommandation[recommandation['score'] > 0]

