from fastapi import FastAPI
from pydantic import BaseModel

class Genre(BaseModel):
    genres: [int]

class Acteur(BaseModel):
    acteurs: [int]

class Film(BaseModel):
    films: [int]

app = FastAPI()

@app.post("/genres/")
def add_genre(genre: Genre):
    return {"genres": genre.genres}

@app.post("/acteurs/")
def add_acteur(acteur: Acteur):
    return {"acteurs": acteur.acteurs}

@app.post("/films/")
def get_film(film: Film):
    return {"films": film.films}

@app.get("/genres/list")
def get_list_genre():
    #sort by name
    return {"genres": [{
        "id": 1,
        "name": "Action"
        },
        {
            "id": 2,
            "name": "Aventure"
        },
        {
            "id": 3,
            "name": "Comédie"
        },
        {
            "id": 4,
            "name": "Drame"
        },
        {
            "id": 5,
            "name": "Fantastique"
        },
        {
            "id": 6,
            "name": "Horreur"
        },
        {
            "id": 7,
            "name": "Policier"
        },
        {
            "id": 8,
            "name": "Romance"
        },
        {
            "id": 9,
            "name": "Science-Fiction"
        },
        {
            "id": 10,
            "name": "Thriller"
        },
        {
            "id": 11,
            "name": "Western"
        },
        {
            "id": 12,
            "name": "Autre"
        }
    ]}

@app.get("/acteurs/list")
def get_list_acteur():
    #sort by name
    return {"acteurs": [{
        "id": 1,
        "name": "Alain Delon"
        },
        {
            "id": 2,
            "name": "Alain Chabat"
        },
        {
            "id": 3,
            "name": "Alain Delon"
        },
        {
            "id": 4,
            "name": "Alain Delon"
        },
        {
            "id": 5,
            "name": "Alain Delon"
        },
        {
            "id": 6,
            "name": "Alain Delon"
        },
        {
            "id": 7,
            "name": "Alain Delon"
        },
        {
            "id": 8,
            "name": "Alain Delon"
        },
        {
            "id": 9,
            "name": "Alain Delon"
        },
        {
            "id": 10,
            "name": "Alain Delon"
        },
        {
            "id": 11,
            "name": "Alain Delon"
        },
        {
            "id": 12,
            "name": "Alain Delon"
        }
    ]}

@app.get("/films/list")
def get_list_film():
    #get list of famous films
    return {"films": [{
        "id": 1,
        "name": "Le Parrain"
        },
        {
            "id": 2,
            "name": "Le Parrain 2"
        },
        {
            "id": 3,
            "name": "Le Parrain 3"
        },
        {
            "id": 4,
            "name": "Forrest Gump"
        },
        {
            "id": 5,
            "name": "Seigneur des Anneaux"
        },
        {
            "id": 6,
            "name": "Pulp Fiction"
        },
        {
            "id": 7,
            "name": "Fight Club"
        },
        {
            "id": 8,
            "name": "Vice-Versa"
        },
        {
            "id": 9,
            "name": "Le Labyrinthe"
        },
        {
            "id": 10,
            "name": "La Ligne Verte"
        },
        {
            "id": 11,
            "name": "Le Seigneur des Anneaux"
        },
        {
            "id": 12,
            "name": "Le Seigneur des Anneaux 2"
        }
    ]}
@app.get("/recommandation")
def get_recommandation():
    return {"films": [{
        "id": 1,
        "name": "Le Parrain"
        },
        {
            "id": 2,
            "name": "Le Parrain 2"
        },
        {
            "id": 3,
            "name": "Le Parrain 3"
        },
        {
            "id": 4,
            "name": "Forrest Gump"
        }]
    }