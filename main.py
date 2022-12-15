from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from Model.Acteurs import Acteurs
from Model.Films import Films
from Model.Genres import Genres
from Model.Recommandation import Recommandation


def make_response(data, status_code=200):
    return Response(content=data.to_json(orient="records"), status_code=status_code, headers={"Content-Type": "application/json"})

class GenreBaseModel(BaseModel):
    genres: List[int]

class ActeurBaseModel(BaseModel):
    acteurs: List[int]

class FilmBaseModel(BaseModel):
    films: List[int]

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="mysupersecretkey", max_age=18000)

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
def add_genre(request: Request, genre: GenreBaseModel):
    request.session["genres"] = genre.genres
    return Response(status_code=201)

@app.post("/acteurs/")
def add_acteur(request: Request, acteur: ActeurBaseModel):
    request.session["acteurs"] = acteur.acteurs
    return Response(status_code=201)

@app.post("/films/")
def add_film(request: Request, film: FilmBaseModel):
    request.session["films"] = film.films
    return Response(status_code=201)

@app.get("/genres/list")
def get_list_genre(request: Request):
    genres = Genres()
    list_genre = genres.get_list_genres()
    return sorted(list_genre, key=lambda d: d['name'])

@app.get("/acteurs/list")
def get_list_acteur():
    acteur = Acteurs()
    list_acteur = acteur.get_list_acteurs().loc[:, ['id', 'name']].sort_values(by=['name'])
    return make_response(list_acteur)

@app.get("/films/list")
def get_list_film():
    #get list of famous films
    film = Films()
    list_film = film.get_list_film().loc[:, ['id', 'title']].sort_values(by=['title'])
    return make_response(list_film)
@app.get("/recommandation")
def get_recommandation(request: Request):
    recommandation = Recommandation(request.session)
    list_recommandation = recommandation.get_list().loc[:, ['id', 'title']]
    return make_response(list_recommandation)

@app.get("/films/autocomplete")
def get_autocomplete_film(request: Request, title: str):
    film = Films()
    list_film = film.get_list_film().loc[:, ['id', 'title']]
    list_film = list_film[list_film['title'].str.contains(title, case=False)]
    return make_response(list_film)

@app.get("/acteurs/autocomplete")
def get_autocomplete_film(request: Request, name: str):
    acteur = Acteurs()
    list_acteur = acteur.get_list_acteurs().loc[:, ['id', 'name']]
    list_acteur = list_acteur[list_acteur['name'].str.contains(name, case=False)]
    return make_response(list_acteur)