from youtube_search import YoutubeSearch
import random
import webbrowser
from song import Song
from playlist_database import Playlistdb
from display import Display


class Playlist:

    def __init__(self, name: str, database: "Playlistdb", display: "Display"):
        self.__name = name
        self.__song = []
        self.__database = database
        self.__display = display
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

    @property
    def display(self):
        return self.__display

    def delete_song(self):
        wanted_date = input("Please input wanted song name: ")
        self.__database.delete_song(self, wanted_date)

    def add_song(self):
        while True:
            song_name = input("Please input song name: ")
            if isinstance(song_name, str) and song_name != "":
                break
            print("Song's name must be string")
            continue
        while True:
            artist = input("Please input artist : ")
            if isinstance(artist, str) and artist != "":
                break
            print("Artist's name must be string")
            continue
        while True:
            duration = input("Please input song name EX(3:21): ")
            if ":" not in duration or not isinstance(duration, str):
                print("Incorrect duration format, Please Try again")
                continue
            break
        while True:
            language = input("Please input song language (not required): ")
            if isinstance(language, str):
                if language == "":
                    language = "None"
                    break
            print("Language must be string, Please Try again")
            continue
        while True:
            url = input("Please input song url (not required): ")
            if isinstance(url, str):
                if url == "":
                    url = "None"
                    break
            print("url must be string")
            continue
        new_song = Song(song_name, artist, duration, language, url)
        user_input = input("Press enter to confirm: ")
        if user_input == "":
            self.__song.append(new_song)
            self.__database.initialize(self)
            print(f"{new_song.name} is added to {self.__name}")
        else:
            print(f"{new_song.name} isn't added to {self.__name}")

    def auto_add_song(self):
        while True:
            user_input = input("Please input song's name: ")
            if user_input == "":
                print("Please input song's name properly")
                continue
            break
        results = YoutubeSearch(user_input, max_results=3).to_dict()
        self.__display.draw_songs_table_youtube(results)
        while True:
            try:
                user_input = int(input("Please choose wanted song's number: "))
                if not 0 < user_input < 4:
                    raise ValueError
            except (ValueError, TypeError):
                print("Song's number must be int and between 1 to 3")
                continue
            break
        new_song = Song(results[user_input - 1]["title"],
                        results[user_input - 1]["channel"],
                        results[user_input - 1]["duration"])
        self.__song.append(new_song)
        self.__database.initialize(self)

    def delete_all_songs(self):
        self.__song = []
        self.__database.initialize(self)
        print("All songs are deleted")

    def shuffle_songs(self):
        random.shuffle(self.__song)
        self.__database.initialize(self)

    def play_a_song(self):
        self.__display.draw_songs_table(self.__song)
        num_songs = len(self.__song)
        while True:
            user_input = int(input("PLease choose wanted song: "))
            if 0 < user_input < num_songs:
                print("Please input correct song's number")
                break
        url = self.__song[user_input - 1].url
        webbrowser.open(url)
