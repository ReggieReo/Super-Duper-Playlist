from song import Song
from playlist_database import Playlistdb


class Playlist:

    def __init__(self, name: str, song: ["Song"], database: "Playlistdb"):
        self.__name = name
        self.__song = song
        self.database = database
        database.initialize(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @property
    def song(self):
        return self.__song

