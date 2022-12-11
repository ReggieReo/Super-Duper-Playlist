from playlist import Playlist, Song, Playlistdb, Display

DATA = Playlistdb()
DISPLAY = Display()


def read_first_menu():
    """
    Reading the user input for the first meny and returning it.
    """
    while True:
        first_function = input("Please choose wanted function (#): ")
        if first_function in ["1", "2", "3", "4"] and \
                isinstance(first_function, str):
            return first_function
        print("Please choose exist function: ")
        input("Press enter to continue: ")
        DISPLAY.clear_screen()
        DISPLAY.draw_first_menu()


def read_wanted_playlist():
    """
    Reading the user wanted playlist, check if the playlist exist,
    and return it to the user.
    """
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
    """
    The first menu when user open the program, which contains See all
    playlists, Open a playlist, Created a new playlist, and Delete a playlist.
    """
    while True:
        DISPLAY.draw_first_menu()
        user_input = read_first_menu()
        if user_input == "1":
            if DATA.get_playlist_info() == {}:
                print("There isn't any playlist. Please create a playlist")
                input("Enter to continue: ")
                DISPLAY.clear_screen()
                continue
            DISPLAY.clear_screen()
            playlist_info = DATA.get_playlist_info()
            DISPLAY.draw_all_playlist(playlist_info)
            input("Press enter to continue: ")
            DISPLAY.clear_screen()
        if user_input == "2":
            if DATA.get_playlist_info() == {}:
                print("There isn't any playlist. Please create a playlist")
                input("Enter to continue: ")
                DISPLAY.clear_screen()
                continue
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
                    want_insert_song = input("Enter y to insert a song: ")
                    if want_insert_song == "y":
                        playlist.add_song()
                        print(f"{playlist_name} is created.")
                        input("Press enter to continue: ")
                        break
                    print(f"{playlist_name} is created.")
                    input("Press enter to continue: ")
                    break
                DISPLAY.clear_screen()
        if user_input == "4":
            if DATA.get_playlist_info() == {}:
                print("There isn't any playlist. Please create a playlist")
                input("Enter to continue: ")
                DISPLAY.clear_screen()
                continue
            DISPLAY.clear_screen()
            playlist_info = DATA.get_playlist_info()
            DISPLAY.draw_all_playlist(playlist_info)
            playlist_name = input("Please input playlist's name :")
            DATA.delete_playlist(playlist_name)
            DISPLAY.clear_screen()
    return opened_playlist


def read_opened_playlist_menu():
    """
    Read the user input for the program's function for the playlist. If the
    user choose correct function return it.
    """
    while True:
        playlist_function = input("Please choose wanted function (#): ")
        if playlist_function in ["1", "2", "3", "4", "5", "6"] \
                and isinstance(playlist_function, str):
            return playlist_function
        print("Please choose exist function. ")
        input("Press enter to continue: ")
        DISPLAY.clear_screen()
        DISPLAY.draw_opened_menu()


def read_add_song():
    """
    Read the user choice for adding a song. If "1" the user will add the song
    manually, and if "2" user will let the program search for the song.
    """
    while True:
        add_song_function = input("Please choose wanted function (#): ")
        if add_song_function in ["1", "2"] and \
                isinstance(add_song_function, str):
            return add_song_function
        print("Please choose exist function. ")
        input("Press enter to continue: ")
        DISPLAY.clear_screen()
        DISPLAY.draw_add_song()


def opened_playlist_menu(opened_playlist):
    """
    This is a menu after user open a playlist, which contains Play a song,
    Add a song, Delete songs, Edit song's information, Get song's information,
    and Close this playlist.
    """
    while True:
        DISPLAY.draw_opened_menu()
        playlist_function = read_opened_playlist_menu()
        if playlist_function == "1":
            DISPLAY.clear_screen()
            opened_playlist.play_a_song()
            DISPLAY.clear_screen()
        if playlist_function == "2":
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
        if playlist_function == "3":
            DISPLAY.clear_screen()
            opened_playlist.delete_song()
            DISPLAY.clear_screen()
        if playlist_function == "4":
            DISPLAY.clear_screen()
            opened_playlist.edit_song_info()
            DISPLAY.clear_screen()
        if playlist_function == "5":
            DISPLAY.clear_screen()
            opened_playlist.share_song()
            DISPLAY.clear_screen()
        if playlist_function == "6":
            break


def main():
    """
    The main script for running the program
    """
    DISPLAY.clear_screen()
    opened_playlist = first_menu()
    opened_playlist_menu(opened_playlist)


if __name__ == "__main__":
    while True:
        main()
        quit_program = input("Do you want to close a program (q to close): ")
        if quit_program in ('q', 'Q'):
            break
        DISPLAY.clear_screen()
