import re
import serial
import movie

#
# Object of type FileDisplayer can be
# used to display media files (avi, mpeg, etc)
# by returning an object of type Serial or Movie
#
class FileDisplayer:
    'Displayer of files of any authorized type'

    #
    # This method take the path of the file
    # in parameter and return an object Serial,
    # an object Movie or a string if none
    #
    def display(self, path):
        path = path.lower();
        # We are looking for something like "xxS01E02xx" -> it's a serial
        match = re.search(r"s\d+e\d+", path);
        if(match):
            return self.displaySerial(match.group(0), path);
        # We are looking for something like "xx2016xx" -> it's a movie
        match = re.search(r"(19|20)\d{2}", path);
        if(match):
            return self.displayMovie(match.group(0), path);
        return path; # If it's none, juste return the path

    #
    # This method take the string which represents the
    # season and episode of the file, and the path, then
    # it return an object Serial created from the infos
    # founded in the path
    #
    def displaySerial(self, seasonAndEpisode, path):
        splitedPath = path.split(seasonAndEpisode);
        # If the path look like "S01E02.avi" -> error
        if(splitedPath[0] == "" or splitedPath[1] == ""):
            return(path);
        name = self.getName(splitedPath[0]);
        season = seasonAndEpisode.split('e')[1];
        episode = seasonAndEpisode.split('e')[0][1:];
        quality = self.getQuality(splitedPath[1]);
        language = self.getLanguage(splitedPath[1]);
        return serial.Serial(path, name, season, episode, quality, language, "");

    #
    # This method take the string which represents the year
    # of the file, and the path, then it return an object Movie
    # created from the infos founded in the path
    #
    def displayMovie(self, year, path):
        splitedPath = path.split(year);
        # If the path look like "2016.avi" -> error
        if(splitedPath[0] == "" or splitedPath[1] == ""):
            return(path);
        name = self.getName(splitedPath[0]);
        quality = self.getQuality(splitedPath[1]);
        language = self.getLanguage(splitedPath[1]);
        return movie.Movie(path, year, name, quality, language, "");

    #
    # Take the left side of the path (xxxS01E02 or xxx2016)
    # and return the name, after processing it a bit
    #
    def getName(self, path):
        # Replace the '.' and '[xxx]' by blank spaces
        name = re.sub(r"\[.*\]", "", path.replace('.', ' '));
        return name;

    #
    # Take the right side of the path (S01E02xxx or 2016xxx)
    # and search some keywords in it to define the quality,
    # then return it ; if none return ""
    #
    def getQuality(self, path):
        quality = re.search(r"(webrip|brrip|hdtv|dvdrip|bdrip|hdrip)", path);
        return "" if quality is None else quality.group(0);

    #
    # Take the right side of the path (S01E02xxx or 2016xxx)
    # and search some keywords in it to define the language,
    # then return it ; if none return ""
    #
    def getLanguage(self, path):
        language = re.search(r"(french|vostfr|truefrench|vo)", path);
        return "" if language is None else language.group(0);
