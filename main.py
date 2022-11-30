from playlist import Playlist, Song, Playlistdb, Display

DATA = Playlistdb()
DISPLAY = Display()


def read_first_menu():
    while True:
        user_input = input("Please choose wanted function: ")
        if user_input in ["1", "2", "3"] and isinstance(user_input, str):
            return user_input
        print("Please choose exist function: ")


def read_wanted_playlist():
    names_playlist = DATA.get_playlist_info()
    while True:
        try:
            playlist_name = input("Please choose a wanted playlist: ")
            wanted_names_playlist = names_playlist[playlist_name]
        except KeyError:
            print("The playlist doesn't exist")
        else:
            return playlist_name, wanted_names_playlist

def first_menu():
    while True:
        DISPLAY.draw_first_menu()
        user_input = read_first_menu()
        if user_input == "1":
            DISPLAY.clear_screen()
            playlist_info = DATA.get_playlist_info()
            DISPLAY.draw_all_playlist(playlist_info)
            input("Press enter to continue: ")
            DISPLAY.clear_screen()
        if user_input == "2":
            DISPLAY.clear_screen()
            playlist_info = DATA.get_playlist_info()
            DISPLAY.draw_all_playlist(playlist_info)
            playlist_name, playlist_songs = read_wanted_playlist()
            song_list = []
            for songs_name, song_info in playlist_songs.items():
                temp_song = Song(songs_name,
                                 song_info["artist"],
                                 song_info["duration"],
                                 song_info["language"],
                                 song_info["url"])
                temp_song.rating = float(song_info["rating"])
                song_list.append(temp_song)
            opened_playlist = Playlist(playlist_name, DATA, DISPLAY, song_list)
            DISPLAY.clear_screen()
            break
        if user_input == "3":
            DISPLAY.clear_screen()
            playlist_name = input("Please insert playlist's name: ")
            if playlist_name in DATA.get_playlist_info():
                print("The playlist is already made")
                input("Enter to continue: ")
                DISPLAY.clear_screen()
            else:
                playlist = Playlist(playlist_name, DATA, DISPLAY)
                print("Do you want to insert a song ?")
                while True:
                    user_input = input("Enter y to insert a song: ")
                    if user_input == "y":
                        playlist.add_song()
                        print(f"{playlist_name} is created.")
                        input("Press enter to continue: ")
                        break
                    print(f"{playlist_name} is created.")
                    input("Press enter to continue: ")
                    break
                DISPLAY.clear_screen()
    return opened_playlist

def main():
    openned_playlist = first_menu()



if __name__ == "__main__":
    playlist1 = Playlist("playlist1", DATA, DISPLAY, [Song("17", "dept", "3:21"), Song("18", "Dept", "3:40")])
    playlist2 = Playlist("playlist2", DATA, DISPLAY, [Song("Plastic love", "Maliya", "4:53")])
    main()
