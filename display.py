from prettytable import PrettyTable


class Display:

    @staticmethod
    def draw_songs_table(song: ["Song"]):
        pass

    @staticmethod
    def draw_songs_table_youtube(search_result):
        table = PrettyTable()
        table.field_names = ["Number", "Song's name", "Artist", "Duration"]
        for index, song in enumerate(search_result):
            table.add_row([index + 1, song["title"], song["channel"],
                           song["duration"]])
        table.align["Song's name"] = "l"
        print(table)

    @staticmethod
    def draw_one_song(song: "Song"):
        pass

    @staticmethod
    def display_all_playlist(database: "Playlistdb"):
        pass
