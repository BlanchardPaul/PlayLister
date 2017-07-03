import requests
import json
import argparse
import pprint

#
# Object of type Movie represents
# a movie file, with in its path its
# name and its year of production
#
class Movie:
    'File of type movie'
    description = "";
    urlImage = "";
    releaseDate = "";

    def __init__(self, path, date, name, quality, language, kind):
        self.path = path;
        self.date = date;
        self.name = name;
        self.quality = quality;
        self.language = language;
        self.kind = kind;

    #
    # Call the API of MovieDB to get the description,
    # image and date of release of the movie ; then set
    # the properties of this instance that correspond
    # !!! DON'T WORK YET !!!
    #
    def getInformationsFromAPI():
        self.name = self.name.replace(' ', '+');
        url = """https://api.themoviedb.org/3/search/
    movie?api_key=5c4b5a2d5706ecedd2d1071928762491&query=""" + self.name;
        response = requests.get(url, {}, verify=False);
        response_json = response.json();
        pprint.pprint(response_json);
