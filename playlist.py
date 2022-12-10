from youtube_search import YoutubeSearch
import random
import webbrowser
from song import Song
from playlist_database import Playlistdb
from display import Display


class Playlist:
    __song: Song

    def __init__(self, name: str, database: "Playlistdb", display: "Display",
                 song=[]):
        self.__name = name
        self.__song = song
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
        self.__display.draw_songs_table(self.__song)
        wanted_delete = input("Please input wanted song name (Name): ")
        for index, song in enumerate(self.__song):
            if song.name == wanted_delete:
                self.__song.pop(index)
        self.__database.delete_song(self, wanted_delete)

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
        new_song = Song(song_name, artist, language, url)
        self.__display.clear_screen()
        self.__display.draw_one_song(new_song)
        user_input = input("Press enter to confirm: ")
        if user_input == "":
            self.__song.append(new_song)
            self.__database.initialize(self)
            print(f"{new_song.name} is added to {self.__name}")
            input("Press enter to continue: ")
        else:
            print(f"{new_song.name} isn't added to {self.__name}")
            input("Press enter to continue: ")

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
        song_url = f'https://youtu.be/' \
                   f'{results[user_input - 1]["url_suffix"].split("=")[1]}'
        new_song = Song(results[user_input - 1]["title"],
                        results[user_input - 1]["channel"],
                        url=song_url)
        self.__song.append(new_song)
        self.__database.initialize(self)
        print(f"{new_song.name} is added to {self.__name}")
        input("Press enter to continue: ")

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
            try:
                user_input = int(input("PLease choose wanted song (#): "))
            except ValueError:
                print("Please input song in integer format.")
                input("Press enter to continue: ")
                continue
            if 0 < user_input <= num_songs:
                url = self.__song[user_input - 1].url
                break
            print("Please input correct song's number")
        webbrowser.open(url)

    def __current_song_information(self, editing_song):
        self.__display.clear_screen()
        print("Current song's information: ")
        self.__display.draw_one_song(editing_song)
        input("Press enter to continue: ")
        self.__display.clear_screen()

    def edit_song_info(self):
        while True:
            self.__display.clear_screen()
            self.__display.draw_songs_table(self.__song)
            try:
                selected_song = int(input("Please choose the song (#): "))
            except ValueError:
                print("Please input song in integer type.")
                input("Press enter to continue: ")
                continue
            num_songs = len(self.__song)
            if 0 < selected_song <= num_songs:
                editing_song = self.__song[selected_song - 1]
                break
        while True:
            self.__display.clear_screen()
            print("You are editing: ")
            self.__display.draw_one_song(editing_song)
            self.__display.draw_edit_song_menu()
            wanted_edit = input("Press choose what to edit (#): ")
            if wanted_edit == "1":
                while True:
                    try:
                        self.__display.clear_screen()
                        print("You are editing this song's name: ")
                        self.__display.draw_one_song(editing_song)
                        new_name = input("Please input new song's name: ")
                        editing_song.name = new_name
                        self.__current_song_information(editing_song)
                        break
                    except TypeError:
                        print("Name must be string type variable")
                        input("Press enter to continue: ")
            elif wanted_edit == "2":
                while True:
                    try:
                        self.__display.clear_screen()
                        print("You are editing this song's artist: ")
                        self.__display.draw_one_song(editing_song)
                        new_artist = input("Please input new song's artist: ")
                        editing_song.artist = new_artist
                        self.__current_song_information(editing_song)
                        break
                    except TypeError:
                        print("Artist must be string type variable")
                        input("Press enter to continue: ")
            elif wanted_edit == "3":
                while True:
                    try:
                        self.__display.clear_screen()
                        print("You are editing this song's language: ")
                        self.__display.draw_one_song(editing_song)
                        new_language = input("Please input new song's "
                                             "language: ")
                        editing_song.language = new_language
                        self.__current_song_information(editing_song)
                        break
                    except TypeError:
                        print("Language must be string type variable")
                        input("Press enter to continue: ")
            elif wanted_edit == "4":
                while True:
                    try:
                        self.__display.clear_screen()
                        print("You are editing this song's url: ")
                        self.__display.draw_one_song(editing_song)
                        new_url = input("Please input new song's url: ")
                        editing_song.url = new_url
                        self.__current_song_information(editing_song)
                        break
                    except TypeError:
                        print("Url must be string type variable")
                        input("Press enter to continue: ")
            elif wanted_edit == "5":
                while True:
                    try:
                        self.__display.clear_screen()
                        print("You are editing this song's rating: ")
                        self.__display.draw_one_song(editing_song)
                        new_rating = float(input("Please input new "
                                                 "song's rating: "))
                        editing_song.rating = new_rating
                        self.__current_song_information(editing_song)
                        break
                    except ValueError:
                        print("Rating of song must be integer or float type "
                              "and between 0 to 5.")
                        input("Press enter to continue: ")
            elif wanted_edit == "6":
                break
            else:
                print("Please input a valid function.")
                input("Press enter to continue: ")
        self.__database.initialize(self)
        self.__display.clear_screen()

    def share_song(self):
        while True:
            self.__display.draw_share_song_menu()
            selected_song_menu = input("Please choose wanted function: ")
            if selected_song_menu == "1":
                self.__display.clear_screen()
                self.__display.draw_songs_table(self.__song)
                while True:
                    try:
                        selected_song = int(input("Please choose the song: "))
                    except ValueError:
                        print("Please input song in integer type:")
                        input("Press enter to continue: ")
                        continue
                    num_songs = len(self.__song)
                    if 0 < selected_song <= num_songs:
                        share_song = self.__song[selected_song - 1]
                        break
                self.__display.clear_screen()
                self.__display.draw_one_song(share_song)
                input("Press enter to continue: ")
                self.__display.clear_screen()
                break
            if selected_song_menu == "2":
                self.__display.clear_screen()
                self.__display.draw_songs_table(self.__song)
                input("Press enter to continue: ")
                self.__display.clear_screen()
                break
            print("Please input correct function: ")
            input("Enter to continue")
            self.__display.clear_screen()
