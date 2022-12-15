import pandas as pd

from Data import Data

class Acteurs:
    def __init__(self):
        self.data = Data.get_instance()

    def get_list_acteurs(self):
        return pd.read_csv("actor_list.csv")