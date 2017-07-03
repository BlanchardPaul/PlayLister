import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import argparse
import pprint
import stringcomparator;

requests.packages.urllib3.disable_warnings(InsecureRequestWarning);

#
# Object of type Movie represents
# a movie file, with in its path its
# name and its year of production
#
class Movie:

    def __init__(self, path, date, name, quality, language, kind):
        self.path = path;
        self.date = date;
        self.name = name;
        self.quality = quality;
        self.language = language;
        self.kind = kind;
        self.description = False;
        self.picture = False;
        
    #
    # Call the API of MovieDB to get the description,
    # image and date of release of the movie ; then set
    # the properties of this instance that correspond
    #
    def getInformationsFromAPI(self):
        nm = self.name.replace(' ', '+');
        url = "https://api.themoviedb.org/3/search/movie?api_key=5c4b5a2d5706ecedd2d1071928762491&year=" + self.date + "&query=""" + nm;
        response = requests.get(url, {}, verify=False);
        response_json = response.json();
        if(response_json["total_results"] == 1):
            self.initFieldsFromResultAPI(response_json["results"][0]);
        elif(response_json["total_results"] > 1):
            for res in response_json["results"]:
                if(stringcomparator.StringComparator.isTheSame(res["title"].lower(), self.name, 6)):
                    self.initFieldsFromResultAPI(res);
                    return;


    def initFieldsFromResultAPI(self, result):
        self.description = result["overview"];
        self.date = result["release_date"];
        self.picture = result["poster_path"];
