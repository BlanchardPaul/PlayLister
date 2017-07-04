import os
import os.path
import glob
import re
import filedisplayer
import movie
import serial
import stringcomparator

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
        self.ListFiles = [file for file in self.getAllFiles(self.path)
                          if file.endswith(tuple(self.AUTHORIZED_EXT))];
  
    def getAllFiles(self, path):  
        fichier=[]  
        l = glob.glob(path+'\\*')  
        for i in l:  
            if os.path.isdir(i): fichier.extend(self.getAllFiles(i))  
            else: fichier.append(i)  
        return fichier

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
            if(stringcomparator.StringComparator.isTheSame(sf.name, file.name, 6)):
                for season in sf.ListSeasons:
                    if(season.number == file.season): # If the serial and the season has been found
                        season.addEpisode(file);
                        return;
                season = serial.SerialSeason(file.season); # If no season has been found
                season.addEpisode(file);
                sf.addSeason(season);
                return;  
        self.insertNewInSerialList(file);
            

    def insertNewInSerialList(self, file):
        season = serial.SerialSeason(file.season);
        season.addEpisode(file);
        serialToAdd = serial.Serial(file.name);
        serialToAdd.addSeason(season);
        self.ListSerialFiles.append(serialToAdd);
                    
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
            serial.getInformationsFromAPI();
            print("name : " + serial.name +
                  ((" | date : " + serial.date) if serial.date else "") +
            ((" | description : " + serial.description) if serial.description else ""));
            for season in serial.ListSeasons:
                print("-- SAISON " + str(season.number));
                for episode in season.ListEpisodes:
                    print("---- EPISODE " + episode.episode);

    def printUnknownList(self):
        print("---- UNKNOWN ----");
        for ukw in self.ListUnknownFiles:
            print(ukw);

d = Directory("C:/Users/spyro/Documents/GitHub/PlayLister/Controllers");
d.initListFiles();
d.displayFilesIntoMediaLists();
d.printSerialList();
