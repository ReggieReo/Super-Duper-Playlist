from song import Song
from playlist_database import Playlistdb


class Playlist:

    def __init__(self, name: str, song: ["Song"], database: "Playlistdb"):
        self.__name = name
        self.__song = song
        self.__database = database
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

    def delete_song(self):
        wanted_date = input("Please input wanted song name: ")
        self.__database.delete_song(self, wanted_date)

    def add_song(self):
        while True:
            song_name = input("Please input song name: ")
            if isinstance(song_name, str) and song_name != "":
                break
            else:
                print("Song's name must be string")
                continue
        while True:
            artist = input("Please input artist : ")
            if isinstance(artist, str) and artist != "":
                break
            else:
                print("Artist's name must be string")
                continue
        while True:
            duration = input("Please input song name ex:(3:21): ")
            if ":" not in duration or not isinstance(duration, str):
                print("Incorrect duration format, Please Try again")
                continue
            else:
                break
        while True:
            language = input("Please input song language (not required): ")
            if isinstance(language, str):
                if language == "":
                    language = "None"
                    break
            else:
                print("Language must be string, Please Try again")
                continue
        while True:
            url = input("Please input song url (not required): ")
            if isinstance(url, str):
                if url == "":
                    url = "None"
                    break
            else:
                print("url must be string")
                continue
        new_song = Song(song_name, artist, duration, language, url)
        print("Please confirm song information")
        print(f"Song's name: {new_song.name}")
        print(f"artist's name: {new_song.artist}")
        print(f"Song's duration: {new_song.duration}")
        print(f"Song's language: {new_song.name}")
        print(f"Song's url: {new_song.url}")
        user_input = input("Press enter to confirm: ")
        if user_input == "":
            self.__song.append(new_song)
            self.__database.initialize(self)
            print(f"{new_song.name} is added to {self.__name}")
        else:
            print(f"{new_song.name} isn't added to {self.__name}")
            pass

    def delete_all_songs(self):
        self.__song = []
        self.__database.initialize(self)
        print("All songs are deleted")
