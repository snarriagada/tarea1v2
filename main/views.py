from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def index(response):
    return render(response,'main/base.html', {})

def v1(response):
    return HttpResponse("view 1")

def home(response):
    episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes").json()

    temp_bb = 1
    temp_bcs = 1

    for e in episodes:
        if e["series"] == "Breaking Bad":
            if int(e["season"]) > temp_bb:
                temp_bb = int(e["season"])

        if e["series"] == "Better Call Saul":
            if int(e["season"]) > temp_bcs:
                temp_bcs = int(e["season"])

    list_bb = []
    list_bcs = []

    for i in range(1,temp_bb+1):
        list_bb.append(i)

    for i in range(1,temp_bcs+1):
        list_bcs.append(i)

    seasons = {"BB": list_bb, "BCS": list_bcs}

    return render(response,'main/home.html', {"seasons": seasons})

def breakingbad(response, s):

    episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad").json()

    episodios_s = []  #guardaremos los episodios de la temporada dada por la url

    for e in episodes:
        if int(e["season"]) == int(s):
            episodios_s.append(e)

    episodios_ordenados = []        
    for i in range(len(episodios_s)):
        episodios_ordenados.append("")

    for e in episodios_s:
        episodios_ordenados[int(e["episode"])-1] = e


    return render(response,'main/breakingbad.html', {"episodios": episodios_ordenados})

def bettercallsaul(response, s):

    episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul").json()

    episodios_s = []  #guardaremos los episodios de la temporada dada por la url

    for e in episodes:
        if int(e["season"]) == int(s):
            episodios_s.append(e)

    episodios_ordenados = []        
    for i in range(len(episodios_s)):
        episodios_ordenados.append("")

    for e in episodios_s:
        episodios_ordenados[int(e["episode"])-1] = e


    return render(response,'main/bettercallsaul.html', {"episodios": episodios_ordenados})




def episodios(response, serie, s, e):

    episodes = {}

    if serie == 0:
        episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad").json()
    else:
        episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul").json()

    episodios_s = []  

    for i in episodes:
        if int(i["season"]) == int(s):
            if int(e) == int(i["episode_id"]):
                episodios_s.append(i)

    personajes = []
    for e in episodios_s:

        for p in e["characters"]:
            aux= p

            string_aux = aux.replace(" ", "+")

            personajes.append([string_aux, aux])
    #hasta aqui tengo personajes = [["walter+white", "walter white"],..., [],....]


    for item in personajes:
        data = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={}".format(item[0])).json()
        data_char = data[0]
        item.append(data_char["char_id"])

    return render(response,'main/episode.html', {"episodios": episodios_s, "personajes": personajes, "serie": serie})

''' ejemplo de personajes:
[['Walter+White', 'Walter White', 1], ['Jesse+Pinkman', 'Jesse Pinkman', 2], ['Skyler+White', 'Skyler White', 3],
 ['Henry+Schrader', 'Henry Schrader', 5], ['Marie+Schrader', 'Marie Schrader', 6], ['Walter+White+Jr.', 'Walter White Jr.', 4],
  ['Tuco+Salamanca', 'Tuco Salamanca', 12]]
  ejemplo de episodios:
  {'episode_id': 6, 'title': 'Crazy Handful of Nothin', 'season': '1', 'air_date': '2008-03-02T00:00:00.000Z', 'characters': 
  ['Walter White', 'Jesse Pinkman', 'Skyler White', 'Henry Schrader', 'Marie Schrader', 'Walter White Jr.',
   'Tuco Salamanca'], 'episode': 6, 'series': 'Breaking Bad'}
'''

def character(response, serie, s):

    data = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/characters/{}".format(s)).json()

    char_data = {"contenido": [], "serie": serie}

    char_data["contenido"] = data




    aux ={}
    aux = char_data["contenido"]

    dict_data = data[0]


    
    nombre = ""
    link_nombre = ""

    nombre = dict_data["name"]
    link_nombre = nombre.replace(" ","+")

    quotes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={}".format(link_nombre)).json()


    char_data["quotes"] = quotes
    


    return render(response,'main/character.html', char_data)


