from playlist import Playlist, Song, Playlistdb, Display

DATA = Playlistdb()
DISPLAY = Display()


def read_first_menu():
    while True:
        user_input = input("Please choose wanted function (#): ")
        if user_input in ["1", "2", "3", "4"] and isinstance(user_input, str):
            return user_input
        print("Please choose exist function: ")
        input("Press enter to continue: ")
        DISPLAY.clear_screen()
        DISPLAY.draw_first_menu()


def read_wanted_playlist():
    names_playlist = DATA.get_playlist_info()
    while True:
        try:
            playlist_name = input("Please choose a wanted playlist (Name): ")
            wanted_names_playlist = names_playlist[playlist_name]
        except KeyError:
            print("The playlist doesn't exist")
            input("Press enter to continue: ")
            DISPLAY.clear_screen()
            DISPLAY.draw_all_playlist(names_playlist)
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
        if user_input == "4":
            DISPLAY.clear_screen()
            playlist_info = DATA.get_playlist_info()
            DISPLAY.draw_all_playlist(playlist_info)
            playlist_name = input("Please input playlist's name :")
            DATA.delete_playlist(playlist_name)
            DISPLAY.clear_screen()
    return opened_playlist


def read_opened_playlist_menu():
    while True:
        user_input = input("Please choose wanted function (#): ")
        if user_input in ["1", "2", "3", "4", "5", "6"] \
                and isinstance(user_input, str):
            return user_input
        print("Please choose exist function. ")
        input("Press enter to continue: ")
        DISPLAY.clear_screen()
        DISPLAY.draw_opened_menu()


def read_add_song():
    while True:
        user_input = input("Please choose wanted function (#): ")
        if user_input in ["1", "2"] and isinstance(user_input, str):
            return user_input
        print("Please choose exist function. ")
        input("Press enter to continue: ")
        DISPLAY.clear_screen()
        DISPLAY.draw_add_song()


def opened_playlist_menu(opened_playlist):
    while True:
        DISPLAY.draw_opened_menu()
        user_input = read_opened_playlist_menu()
        if user_input == "1":
            DISPLAY.clear_screen()
            opened_playlist.play_a_song()
            DISPLAY.clear_screen()
        if user_input == "2":
            DISPLAY.clear_screen()
            DISPLAY.draw_add_song()
            user_add_song = read_add_song()
            if user_add_song == "1":
                DISPLAY.clear_screen()
                opened_playlist.add_song()
                DISPLAY.clear_screen()
            if user_add_song == "2":
                DISPLAY.clear_screen()
                opened_playlist.auto_add_song()
                DISPLAY.clear_screen()
            DISPLAY.clear_screen()
        if user_input == "3":
            DISPLAY.clear_screen()
            opened_playlist.delete_song()
            DISPLAY.clear_screen()
        if user_input == "4":
            DISPLAY.clear_screen()
            opened_playlist.edit_song_info()
            DISPLAY.clear_screen()
        if user_input == "5":
            DISPLAY.clear_screen()
            opened_playlist.share_song()
            DISPLAY.clear_screen()
        if user_input == "6":
            break


def main():
    DISPLAY.clear_screen()
    opened_playlist = first_menu()
    opened_playlist_menu(opened_playlist)


if __name__ == "__main__":
    while True:
        main()
        user_input = input("Do you want to close a program (q to close): ")
        if user_input == "q" or user_input == "Q":
            break
        DISPLAY.clear_screen()
