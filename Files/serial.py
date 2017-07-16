import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import argparse
import pprint
import os
import Utils
from Utils import stringcomparator

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#
# Object of type SerialEpisode represents
# an episode of a season of the serial,
# with also in its path its quality and
# language
#
class SerialEpisode:
    'File of type serial episode'

    def __init__(self, path, name, season, episode, quality, language, kind):
        self.path = path
        self.name = name
        self.season = season
        self.episode = episode
        self.quality = quality
        self.language = language
        self.kind = kind

    def read(self):
        os.startfile(self.path)
    

#
# Object of type SerialSeason represents
# a season of the serial, with the number
# and a list that contains the episodes
#
class SerialSeason:
    'Abstract object that represents a season of a serial'
    
    def __init__(self, number):
        self.number = number
        self.ListEpisodes = []

    def addEpisode(self, episode):
        self.ListEpisodes.append(episode)
        self.ListEpisodes = sorted(self.ListEpisodes, key=lambda ep: ep.episode)
        

#
# Object of type Serial represents
# a serial, with the name and a list
# that contains the seasons
#
class Serial:
    'Abstract object that represents a serial'

    def __init__(self, name):
        self.name = name
        self.ListSeasons = []
        self.description = False
        self.picture = False
        self.date = False

    def addSeason(self, season):
        self.ListSeasons.append(season)
        self.ListSeasons = sorted(self.ListSeasons, key=lambda season: season.number)

    def getInformationsFromAPI(self):
        nm = self.name.replace(' ', '+')
        url = "https://api.themoviedb.org/3/search/tv?api_key=5c4b5a2d5706ecedd2d1071928762491&query=" + nm
        response = requests.get(url, {}, verify=False)
        response_json = response.json()
        if(response_json["total_results"] == 1):
            self.initFieldsFromResultAPI(response_json["results"][0])
        elif(response_json["total_results"] > 1):
            for res in response_json["results"]:
                if(stringcomparator.StringComparator.isTheSame(res["name"].lower(), self.name, 6)):
                   self.initFieldsFromResultAPI(res)
                   return

    def initFieldsFromResultAPI(self, result):
        self.description = result["overview"]
        self.date = result["first_air_date"]
        self.picture = result["poster_path"]
