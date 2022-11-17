from song import Song


class Playlist:

    def __init__(self, name: str, song: ["Song"]):
        self.__name = name
        self.__song = song
