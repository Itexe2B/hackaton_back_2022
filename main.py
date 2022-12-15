from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

import Model.Acteurs as Acteurs
import Model.Films as Films
import Model.Genres as Genres
class Genre(BaseModel):
    genres: List[int]

class Acteur(BaseModel):
    acteurs: List[int]

class Film(BaseModel):
    films: List[int]

app = FastAPI()
# Allow all origins
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
