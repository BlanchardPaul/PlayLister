import re
import Files
from Files import movie, serial


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
        name = path.split('\\')[-1].lower()
        # We are looking for something like "xxS01E02xx" -> it's a serial
        match = re.search(r"s\d+e\d+", name)
        if(match):
            return self.displaySerial(match.group(0), name, path)
        # We are looking for something like "xx2016xx" -> it's a movie
        match = re.search(r"(19|20)\d{2}", name)
        if(match):
            return self.displayMovie(match.group(0), name, path)
        return path # If it's none, juste return the path

    #
    # This method take the string which represents the
    # season and episode of the file, and the path, then
    # it return an object SerialEpisode created from the infos
    # founded in the path
    #
    def displaySerial(self, seasonAndEpisode, name, path):
        splitedName = name.split(seasonAndEpisode)
        # If the name look like "S01E02.avi" -> error
        if(splitedName[0] == "" or splitedName[1] == ""):
            return(path)
        title = self.getTitle(splitedName[0])
        episode = seasonAndEpisode.split('e')[1]
        season = seasonAndEpisode.split('e')[0][1:]
        quality = self.getQuality(splitedName[1])
        language = self.getLanguage(splitedName[1])
        return serial.SerialEpisode(path, title, int(season), episode, quality, language, "")

    #
    # This method take the string which represents the year
    # of the file, and the path, then it return an object Movie
    # created from the infos founded in the path
    #
    def displayMovie(self, year, name, path):
        splitedName = name.split(year)
        # If the name look like "2016.avi" -> error
        if(splitedName[0] == "" or splitedName[1] == ""):
            return(path)
        title = self.getTitle(splitedName[0])
        quality = self.getQuality(splitedName[1])
        language = self.getLanguage(splitedName[1])
        return movie.Movie(path, year, title, quality, language, "")

    #
    # Take the left side of the path (xxxS01E02 or xxx2016)
    # and return the name, after processing it a bit
    #
    def getTitle(self, name):
        # Replace the '.' and '[xxx]' by blank spaces
        title = re.sub(r"\[.*\]", "", name.replace('.', ' '))
        return title

    #
    # Take the right side of the path (S01E02xxx or 2016xxx)
    # and search some keywords in it to define the quality,
    # then return it  if none return ""
    #
    def getQuality(self, name):
        quality = re.search(r"(webrip|brrip|hdtv|dvdrip|bdrip|hdrip|blueray|bluray)", name)
        return "" if quality is None else quality.group(0)

    #
    # Take the right side of the path (S01E02xxx or 2016xxx)
    # and search some keywords in it to define the language,
    # then return it  if none return ""
    #
    def getLanguage(self, name):
        language = re.search(r"(french|vostfr|truefrench|vo|fr|vff)", name)
        return "" if language is None else language.group(0)
