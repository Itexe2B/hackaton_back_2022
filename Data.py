import pandas as pd

class Data:
    __instance = None
    df_movies = None
    df_credits = None
    @staticmethod
    def get_instance():
        if Data.__instance is None :
            print("Création du service")
            Data.__instance = Data()
        return Data.__instance

    def __init__(self):
        Data.df_movies = pd.read_csv("tmdb_5000_movies.csv")
        Data.df_credits = pd.read_csv("tmdb_5000_credits.csv")