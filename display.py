from prettytable import PrettyTable


class Display:

    @staticmethod
    def draw_songs_table(list_songs: ["Song"]):
        table = PrettyTable()
        table.field_names = ["Song's number", "Song's name", "Artist",
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
        table.field_names = ["Number", "Song's name", "Artist", "Duration"]
        for index, song in enumerate(search_result):
            table.add_row([index + 1, song["title"], song["channel"],
                           song["duration"]])
        table.align["Song's name"] = "l"
        print(table)

    @staticmethod
    def display_all_playlist(database: "Playlistdb"):
        pass
