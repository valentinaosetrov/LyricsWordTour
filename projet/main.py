# imports
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
import os
from pydantic import BaseModel
from typing import Literal, Optional
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
import re
import requests


app = FastAPI()

# Function to extract places from lyrics
def extract_places(lyrics):
    places = re.findall(r'#(.*?)#', lyrics)
    return places

# Function to geocode a place using OpenStreetMap Nominatim API
def geocode_place(place):
    if place.lower() == "l.a." or place.lower() == "la":
        place = "Los Angeles"
    elif place.lower() == "sunrise boulevard":
        place = "Sunrise Blvd"
    elif place.lower() == "cornelia street":
        place = "Cornelia Street London"
    
    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": place, "format": "json", "limit": 1}
    )
    data = response.json()
    if data:
        lat_lng = {"lat": float(data[0]["lat"]), "lng": float(data[0]["lon"])}
        return lat_lng
    else:
        return None


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

# Define the route to handle form submission
@app.post("/submit")
async def submit_form(request: Request):
    # Redirect to the lyrics.html page with the checkbox value
    form_data = await request.form() 
    t = form_data.get("title")
    for song in SONG_DATABASE : 
        if song["title"] == t : 
            paroles = song["lyrics"]

    places_with_coordinates = []
    for line in paroles:
        places = extract_places(line)
        if places != [] :
            print("Places from lyrics:", places)
        for place in places:
            coordinates = geocode_place(place)
            if coordinates:
                places_with_coordinates.append({"name": place, "lat": coordinates["lat"], "lng": coordinates["lng"]})

    print("Places with coordinates:", places_with_coordinates)
    return templates.TemplateResponse("lyrics.html", {"titre" : t, "lyrics": paroles, "coordinates":places_with_coordinates, "request" : request})