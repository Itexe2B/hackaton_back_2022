import pandas as pd

from Data import Data

class Genres:
    def __init__(self):
        self.data = Data.get_instance()

    def get_list_genres(self):
        list_genre = []
        id_list_exclude = []
        for genres in self.data.df_movies['genres']:
            for genre in genres:
                if genre['id'] not in id_list_exclude:
                    id_list_exclude.append(genre['id'])
                    list_genre.append(genre)
        return list_genre