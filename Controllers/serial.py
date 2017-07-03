#
# Object of type SerialEpisode represents
# an episode of a season of the serial,
# with also in its path its quality and
# language
#
class SerialEpisode:
    'File of type serial episode'

    def __init__(self, path, name, season, episode, quality, language, kind):
        self.path = path;
        self.name = name;
        self.season = season;
        self.episode = episode;
        self.quality = quality;
        self.language = language;
        self.kind = kind;

#
# Object of type SerialSeason represents
# a season of the serial, with the number
# and a list that contains the episodes
#
class SerialSeason:
    'Abstract object that represents a season of a serial'
    
    def __init__(self, number):
        self.number = number;
        self.ListEpisodes = [];

    def addEpisode(self, episode):
        self.ListEpisodes.append(episode);

    def sort(self):
        self.ListEpisodes = sorted(self.ListEpisodes, key=lambda ep: ep.episode);

#
# Object of type Serial represents
# a serial, with the name and a list
# that contains the seasons
#
class Serial:
    'Abstract object that represents a serial'
    ### THERE METHOD CALLING API

    def __init__(self, name):
        self.name = name;
        self.ListSeasons = [];

    def addSeason(self, season):
        self.ListSeasons.append(season);

    def sort(self):
        self.ListSeasons = sorted(self.ListSeasons, key=lambda season: season.number);


