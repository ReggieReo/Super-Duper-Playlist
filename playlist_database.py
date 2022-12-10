import json


class Playlistdb:
    def __init__(self):
        try:
            with open("playlists.json", "r") as data_file:
                if data_file is None:
                    raise FileNotFoundError
        except (FileNotFoundError, json.JSONDecodeError):
            with open("playlists.json", "w") as data_file:
                empty_playlist = {}
                json.dump(empty_playlist, data_file, indent=4)
                print("Created playlists.json")

    @staticmethod
    def __make_song_dicts(playlist: "Plalist"):
        songs_dict = {}
        for song in playlist.song:
            temp = {song.name: {
                "artist": song.artist,
                "language": song.language,
                "url": song.url,
                "rating": song.rating}
            }
            songs_dict.update(temp)
        return songs_dict

    def initialize(self, playlist: "Playlist"):
        new_data = {playlist.name: self.__make_song_dicts(playlist)}
        try:
            with open("playlists.json", "r") as data_file:
                playlist_db = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("playlists.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            playlist_db.update(new_data)
            with open("playlists.json", "w") as data_file:
                json.dump(playlist_db, data_file, indent=4)

    @staticmethod
    def delete_playlist(playlist_name: str):
        try:
            with open("playlists.json", "r") as data_file:
                playlist_db = json.load(data_file)
            playlist_db.pop(playlist_name)
            with open("playlists.json", "w") as data_file:
                json.dump(playlist_db, data_file, indent=4)
            print(f"{playlist_name} is deleted")
            input("Press enter to continue: ")
        except KeyError:
            print(f"{playlist_name} doesn't exist")
            input("Press enter to continue: ")

    @staticmethod
    def delete_song(playlist: 'Playlist', song_name: str):
        try:
            with open("playlists.json", "r") as data_file:
                playlist_db = json.load(data_file)
            playlist_db[playlist.name].pop(song_name)
            with open("playlists.json", "w") as data_file:
                json.dump(playlist_db, data_file, indent=4)
            print(f"{song_name} is deleted")
            input("Please enter to continue: ")
        except KeyError:
            print(f"{song_name} doesn't exist")
            input("Please enter to continue: ")

    @staticmethod
    def get_playlist_info():
        try:
            with open("playlists.json", "r") as data_file:
                data_file = json.load(data_file)
                if data_file is None:
                    raise FileNotFoundError
        except (FileNotFoundError, json.JSONDecodeError):
            empty_playlist = {}
            json.dump(empty_playlist, data_file, indent=4)
            print("Created playlists.json")
            input("Enter to continue: ")
        else:
            return data_file
