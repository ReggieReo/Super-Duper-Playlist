import json


class Playlistdb:
    """
    This class is made for reading and writing information of the playlist
    class.
    """

    def __init__(self):
        """
        When Initializing this class, it will check weather ot not
        playlists.json exists. If not it will create playlists.json and
        put empty playlist in the file.
        """
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
    def __make_song_dicts(playlist: "Playlist"):
        """
        This method is used for turning list of Song class into dict, so it can
        be used to save into playlists.json.

        :param playlist: playlist class that contains list of song class.
        :return: Dict of song class' information
        """
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
        """
        Everytime there are changes in playlist class' information, this method
        will save the changes into the file.

        param playlist: Playlist class
        """
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
        """
        This method deletes playlist in playlists.json from the given
        playlist's name
        :param playlist_name:
        """
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
        """
        Delete song from the given song name in playlists.json file.

        :param playlist: Playlist class
        :param song_name: Name of the song
        """
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
        """
        Return all information in playlists.json, which contains all
        playlist information.
        :return: Information contains all playlists.json data.
        """
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
