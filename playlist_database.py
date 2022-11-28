import json


class Playlistdb:

    @staticmethod
    def __make_song_dicts(playlist: "Plalist"):
        songs_dict = {}
        for song in playlist.song:
            temp = {song.name: {
                "artist": song.artist,
                "duration": song.duration,
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
        except (FileNotFoundError, ValueError):
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
        except KeyError:
            print(f"{playlist_db} doesn't exist")

    @staticmethod
    def delete_song(playlist: 'Playlist', song_name: str):
        try:
            with open("playlists.json", "r") as data_file:
                playlist_db = json.load(data_file)
            playlist_db[playlist.name].pop(song_name)
            with open("playlists.json", "w") as data_file:
                json.dump(playlist_db, data_file, indent=4)
            print(f"{song_name} is deleted")
        except KeyError:
            print(f"{song_name} doesn't exist")

