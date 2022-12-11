from os import system, name
from prettytable import PrettyTable


class Display:
    """
    This class is used for drawing menu, or given information into a table.
    """

    @staticmethod
    def draw_songs_table(list_songs: ["Song"]):
        """
        From the given list of songs object draw a table contains all songs'
        information.
        """
        table = PrettyTable()
        table.field_names = ["#", "Song's name", "Artist",
                             "Language", "url", "Rating"]
        for index, song in enumerate(list_songs):
            table.add_row([index + 1, song.name, song.artist,
                           song.language, song.url, song.rating])
        print(table)

    @staticmethod
    def draw_one_song(song: "Song"):
        """
        From the given song object draw a table contains all song's
        information.
        """
        table = PrettyTable()
        table.field_names = ["Song's name", "Artist", "Language", "url",
                             "Rating"]
        table.add_row([song.name, song.artist, song.language,
                       song.url, song.rating])
        print(table)

    @staticmethod
    def draw_songs_table_youtube(search_result):
        """
        From the search result, which is YouTube search result. Draw 3 songs'
        information that will let the user choose later.
        """
        table = PrettyTable()
        table.field_names = ["#", "Song's name", "Artist"]
        for index, song in enumerate(search_result):
            table.add_row([index + 1, song["title"], song["channel"]])
        table.align["Song's name"] = "l"
        print(table)

    @staticmethod
    def draw_all_playlist(database: "Playlistdb"):
        """
        Get the data from the playlist database's method and draw all playlist
        contains in playlist.json.
        """
        table = PrettyTable()
        table.field_names = ["#", "Playlist's name"]
        for index, playlist_name in enumerate(database.keys()):
            table.add_row([index + 1, playlist_name])
        print(table)

    @staticmethod
    def draw_first_menu():
        """
        Drawing the first menu when user open the program.
        """
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
        """
        Drawing a menu after user chose to open a playlist.
        """
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
        """
        Drawing a table for the adding song menu.
        """
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "Add a song"],
                        ["2", "Auto add a song"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def draw_edit_song_menu():
        """
        Drawing a table for the editing song's information menu.
        """
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
        """
        Drawing a table for the sharing song menu.
        """
        table = PrettyTable()
        table.field_names = ["#", "Function"]
        table.add_rows([["1", "Share single song"],
                        ["2", "Share all song"]])
        table.align["Function"] = "l"
        print(table)

    @staticmethod
    def clear_screen():
        """
        Clear the terminal screen.
        """
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
