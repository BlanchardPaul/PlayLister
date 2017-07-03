import os
import re
import filedisplayer
import movie
import serial

class Directory:
    'A directory that contains files of any types'

    AUTHORIZED_EXT = [ ".avi", ".mpeg", ".pdf" ];
    
    def __init__(self, path):
        self.path = path;
        self.ListFiles = [];
        self.ListMovieFiles = [];
        self.ListSerialFiles = [];
        self.ListUnknownFiles = [];

    def initListFiles(self):
        if not (os.path.isdir(self.path)):
            print("The given path is not a directory.");
            return False;
        # We are looking for the files that end with an extension from AUTHORIZED_EXT
        self.ListFiles = [file for file in os.listdir(self.path)
                          if file.endswith(tuple(self.AUTHORIZED_EXT))];

    def displayFilesIntoMediaLists(self):
        fd = filedisplayer.FileDisplayer();
        for f in self.ListFiles:
            file = fd.display(f);
            if (isinstance(file, movie.Movie)):
                self.ListMovieFiles.append(file);
            elif (isinstance(file, serial.SerialEpisode)):
                self.displayInsertionInSerialList(file);
            else:
                self.ListUnknownFiles.append(file);

    def displayInsertionInSerialList(self, file):
        for sf in self.ListSerialFiles:
            if(self.isTheSame(sf.name, file.name)):
                for season in sf.ListSeasons:
                    if(season.number == file.season): # If the serial and the season has been found
                        season.addEpisode(file);
                        season.sort();
                        return;
                season = serial.SerialSeason(file.season); # If no season has been found
                season.addEpisode(file);
                sf.addSeason(season);
                sf.sort();
                return;  
        self.insertNewInSerialList(file);
            

    def insertNewInSerialList(self, file):
        season = serial.SerialSeason(file.season);
        season.addEpisode(file);
        serialToAdd = serial.Serial(file.name);
        serialToAdd.addSeason(season);
        self.ListSerialFiles.append(serialToAdd);
            
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
        return (index > len(name)/10*6 and index > len(nameToCompare)/10*6);
                    
    def printMovieList(self):
        print("---- MOVIES ----");
        for movie in self.ListMovieFiles:
            movie.getInformationsFromAPI();
            print("");
            print("name : " + movie.name + " | date : " + movie.date +
                  " | quality : " + movie.quality + " | language : " + movie.language +
                  ((" | description : " + movie.description) if movie.description else ""));
            

    def printSerialList(self):
        print("---- SERIAL ----");
        for serial in self.ListSerialFiles:
            print(serial.name);
            for season in serial.ListSeasons:
                print("-- SAISON " + str(season.number));
                for episode in season.ListEpisodes:
                    print("---- EPISODE " + episode.episode);

    def printUnknownList(self):
        print("---- UNKNOWN ----");
        for ukw in self.ListUnknownFiles:
            print(ukw);
        
    def printl(self, file):
        print("nom " + file.name + " episode " + file.episode + " saison " + str(file.season));

d = Directory("C:/Users/spyro/Desktop/okok/okok");
d.initListFiles();
d.displayFilesIntoMediaLists();
d.printMovieList();
