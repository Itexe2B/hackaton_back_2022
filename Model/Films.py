import pandas as pd
from Data import Data

class Films:
    def __init__(self):
        self.data = Data.get_instance()

    def get_list_film(self):
        return self.data.df_movies
