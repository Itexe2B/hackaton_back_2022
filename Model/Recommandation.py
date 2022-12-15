import pandas as pd
import json
import numpy as np
from Data import Data

class Recommandation:
    def __init__(self, session):
        self.session = session
        self.data = Data.get_instance()

    def get_list(self):
        list_genre = self.session['genres']
        list_films = self.session['films']
        list_acteur = self.session['acteurs']
        recommandation = self.data.df_movies.loc[:, ['id', 'title', 'genres', 'vote_average', 'popularity']]
        recommandation['score'] = 0
        #add 10 to score if the genre is in the list of genre
        for genre in list_genre:
            recommandation['score'] = np.where(recommandation['genres']
                                               .apply(lambda item: genre in json.loads(item)),
                                               recommandation['score'] + 10,
                                               recommandation['score'])

        #add 5 to score if the film is in the list of film
        for film in list_films:
            recommandation['score'] = np.where(recommandation['id'] == film,
                                               recommandation['score'] + 5,
                                               recommandation['score'])

        #add 1 to score if the actor is in the list of actor
        for acteur in list_acteur:
            recommandation['score'] = np.where(self.data.df_credits['cast']
                                               .apply(lambda item: acteur in json.loads(item)),
                                               recommandation['score'] + 1,
                                               recommandation['score'])

        recommandation = recommandation.sort_values(by=['score', 'vote_average', 'popularity'], ascending=False)
        return recommandation
