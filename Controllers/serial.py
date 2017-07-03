#
# Object of type Serial represents
# an episode of a season of the serial,
# with also in its path its quality and
# language
#
class Serial:
    'File of type serial'

    def __init__(self, path, name, season, episode, quality, language, kind):
        self.path = path;
        self.name = name;
        self.season = season;
        self.episode = episode;
        self.quality = quality;
        self.language = language;
        self.kind = kind;
