from prettytable import PrettyTable
from os import system, name


class Display:

    @staticmethod
    def draw_songs_table(list_songs: ["Song"]):
        table = PrettyTable()
        table.field_names = ["#", "Song's name", "Artist",
                             "Language", "url", "Rating"]
        for index, song in enumerate(list_songs):
            table.add_row([index + 1, song.name, song.artist,
                           song.language, song.url, song.rating])
        print(table)

    @staticmethod
    def draw_one_song(song: "Song"):
        table = PrettyTable()
        table.field_names = ["Song's name", "Artist", "Language", "url",
                             "Rating"]
        table.add_row([song.name, song.artist, song.language,
                       song.url, song.rating])
        print(table)

    @staticmethod
    def draw_songs_table_youtube(search_result):
        table = PrettyTable()
        table.field_names = ["#", "Song's name", "Artist"]
        for index, song in enumerate(search_result):
            table.add_row([index + 1, song["title"], song["channel"]])
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
                        ["3", "Created a new playlist"],
                        ["4", "Delete a playlist"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def draw_opened_menu():
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "Play a song"],
                        ["2", "Add a song"],
                        ["3", "Delete songs"],
                        ["4", "Edit song's information"],
                        ["5", "Get song's information"],
                        ["6", "Close this playlist"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def draw_add_song():
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "Add a song"],
                        ["2", "Auto add a song"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def draw_edit_song_menu():
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "Edit song's name"],
                        ["2", "Edit song's artist"],
                        ["3", "Edit song's language"],
                        ["4", "Edit song's url"],
                        ["5", "Edit song's rating"],
                        ["6", "Stop editing"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def draw_share_song_menu():
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "Share single song"],
                        ["2", "Share all song"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def clear_screen():
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
