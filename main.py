from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from Model.Acteurs import Acteurs
from Model.Films import Films
from Model.Genres import Genres
from Model.Recommandation import Recommandation
from Session import Session


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
def add_genre(genre: GenreBaseModel):
    #request.session["genres"] = genre.genres
    Session.get_instance().put_session("genres", genre.genres)
    return Response(status_code=201)

@app.post("/acteurs/")
def add_acteur(acteur: ActeurBaseModel):
    Session.get_instance().put_session("acteurs", acteur.acteurs)
    return Response(status_code=201)

@app.post("/films/")
def add_film(film: FilmBaseModel):
    Session.get_instance().put_session("films", film.films)
    return Response(status_code=201)

@app.get("/genres/list")
def get_list_genre():
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
def get_recommandation():
    recommandation = Recommandation()
    list_recommandation = recommandation.get_list().loc[:, ['id', 'title', 'score']]
    return make_response(list_recommandation.iloc[:50])

@app.get("/films/autocomplete")
def get_autocomplete_film(title: str):
    film = Films()
    list_film = film.get_list_film().loc[:, ['id', 'title']]
    list_film = list_film[list_film['title'].str.contains(title, case=False)]
    if list_film.empty:
        return []
    return make_response(list_film)

@app.get("/acteurs/autocomplete")
def get_autocomplete_film(name: str):
    acteur = Acteurs()
    list_acteur = acteur.get_list_acteurs().loc[:, ['id', 'name']]
    list_acteur = list_acteur[list_acteur['name'].str.contains(name, case=False).fillna(False)]

    if list_acteur.empty:
        return []

    return make_response(list_acteur)

@app.get("/films/infos")
def get_infos_film(id: int):
    film = Films()
    thumbnail, url, id_video = film.get_infos(id)
    print(id_video)

    return {
        "thumbnail": thumbnail,
        "url": url,
        "genres": film.data.df_movies.loc[film.data.df_movies['id'] == id, 'genres'].values[0],
        "description": film.data.df_movies.loc[film.data.df_movies['id'] == id, 'overview'],
        "preview_link": film.get_preview(id, id_video)
            }