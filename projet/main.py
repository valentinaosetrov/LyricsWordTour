# Nouveaux imports
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import json
import os

# Nouveaus imports
from pydantic import BaseModel
from typing import Literal, Optional
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse



# # Définition d'un objet Recette
# class Recette(BaseModel):
#     nom: str
#     type: Literal["végétarien", "végan", "carné"] # Le type Literal définit des constantes
#     id: Optional[str] = uuid4().hex

app = FastAPI()

# Fonction sans route qui va se charger de traiter les données
# # Prend en paramètre en objet Recette et l'écrit dans le JSON
# def util_ajouter_recette(recette: Recette):
#     # Générer un ID
#     recette.id = uuid4().hex
#     # Transformer l'objet Recette au format JSON
#     json_recette = jsonable_encoder(recette)
#     # Ajouter l'élément au JSON initial (stocké dans la variable globale RECETTE_DATABASE)
#     RECETTE_DATABASE.append(json_recette)
#     # Écrire ce nouveau JSON dans le fichier externe
#     with open(RECETTE_DATABASE_FILE, "w") as f:
#         json.dump(RECETTE_DATABASE, f)

# A placer sous app = FastAPI(). Cette ligne active le moteur de template Jinja et indique que les templates HTML seront stockés dans le dossier "templates"
templates = Jinja2Templates(directory="site")

# Cette ligne indique que les fichiers statiques (images, css) seront placés dans le dossier nommé "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

# Chargement de la base de données JSON
SONG_DATABASE_FILE = "data.json"

if os.path.exists(SONG_DATABASE_FILE):
    with open(SONG_DATABASE_FILE, "r") as f:
        SONG_DATABASE = json.load(f)

# Modification de la route pour renvoyer du HTML
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/song_list", response_class=HTMLResponse)
async def song_list(request: Request):
    return templates.TemplateResponse("song_list.html", {"songs": SONG_DATABASE, "request" : request})

# Define the route to serve the lyrics page
@app.get("/lyrics", response_class=HTMLResponse)
async def lyrics(request: Request):
    return templates.TemplateResponse("lyrics.html", {"request": request})

# @app.get("/lyrics", response_class=HTMLResponse)
# async def song_list(request: Request):
#     return templates.TemplateResponse("lyrics.html", {"songs": SONG_DATABASE, "request" : request})

# Define the route to handle form submission
@app.post("/submit")
async def submit_form(request: Request):
    # Redirect to the lyrics.html page with the checkbox value
    form_data = await request.form() 
    t = form_data.get("title")
    for song in SONG_DATABASE : 
        if song["title"] == t : 
            paroles = song["lyrics"]
    return templates.TemplateResponse("lyrics.html", {"titre" : t, "lyrics": paroles, "request" : request})








# @app.get("/ajout-recette") #afficher les templates
# async def ajout_recette(request: Request):
#     return templates.TemplateResponse("ajouter_recette.html", {"request": request})

# @app.post("/song_list", response_class=HTMLResponse) #modifier les templates
# async def song_choice(request: Request):
#     # On récupère les valeurs du formulaire
#     # form_data = await request.form()
#     # titre = form_data.get('title') # valeur du champ name="titre" dans le formulaire HTML 
#     return RedirectResponse(url=f"/lyrics?checkbox_value={checkbox_value}")


#     # On crée un nouvel objet Recette pour l'ajouter dans la base
#     recette = Recette(nom=titre, type=type_recette)

#     # On fait appel à la fonction extérieure pour gérer l'ajout dans la BDD
#     util_ajouter_recette(recette)

    # return templates.TemplateResponse("ajouter_recette.html", {"request": request})