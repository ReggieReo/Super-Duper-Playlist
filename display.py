from prettytable import PrettyTable
from os import system, name


class Display:

    @staticmethod
    def draw_songs_table(list_songs: ["Song"]):
        table = PrettyTable()
        table.field_names = ["#", "Song's name", "Artist",
                             "Duration", "Language", "url", "Rating"]
        for index, song in enumerate(list_songs):
            table.add_row([index + 1, song.name, song.artist, song.duration,
                           song.language, song.url, song.rating])
        print(table)

    @staticmethod
    def draw_one_song(song: "Song"):
        table = PrettyTable()
        table.field_names = ["Song's name", "Artist", "Duration", "Language",
                             "url", "Rating"]
        table.add_row([song.name, song.artist, song.duration, song.language,
                       song.url, song.rating])
        print(table)

    @staticmethod
    def draw_songs_table_youtube(search_result):
        table = PrettyTable()
        table.field_names = ["#", "Song's name", "Artist", "Duration"]
        for index, song in enumerate(search_result):
            table.add_row([index + 1, song["title"], song["channel"],
                           song["duration"]])
        table.align["Song's name"] = "l"
        print(table)

    @staticmethod
    def draw_all_playlist(database: "Playlistdb"):
        table = PrettyTable()
        table.field_names = ["#", "Playlist's name"]
        for index, playlist_name in enumerate(database.keys()):
            table.add_row([index + 1, playlist_name])
        print(table)

    @staticmethod
    def draw_first_menu():
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "See all playlists"],
                        ["2", "Open a playlist"],
                        ["3", "Created a new playlist"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def clear_screen():
        if name == 'nt':
            # for windows
            system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
