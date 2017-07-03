import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import argparse
import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning);

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
        
    def isTheSame(self, name, nameToCompare):
        index = 0;
        nameList = list(name);
        nameToCompareList = list(nameToCompare);
        for n in nameList:
            for m in nameToCompareList:
                if(n == m):
                    index += 1;
                    del nameToCompareList[nameToCompareList.index(m)];
                    break;
        #print("index name : " + str(index) + "/" + str(len(name)) + " index name to : " + str(index) + "/" + str(len(nameToCompare)));
        return (index > len(name)/10*6 and index > len(nameToCompare)/10*6);

    #
    # Call the API of MovieDB to get the description,
    # image and date of release of the movie ; then set
    # the properties of this instance that correspond
    #
    def getInformationsFromAPI(self):
        nm = self.name.replace(' ', '+');
        url = """https://api.themoviedb.org/3/search/movie?api_key=5c4b5a2d5706ecedd2d1071928762491&year=""" + self.date + "&query=""" + nm;
        response = requests.get(url, {}, verify=False);
        response_json = response.json();
        result = False;
        if(response_json["total_results"] < 1):
            self.description = False;
            self.picture = False;
            return;
        elif(response_json["total_results"] == 1):
            result = response_json["results"][0];
        else:
            for res in response_json["results"]:
                if(self.isTheSame(res["title"].lower(), self.name)):
                    result = res;
        if not(result):
            return;
        self.description = result["overview"];
        self.date = result["release_date"];
        self.picture = result["poster_path"];
