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
    nums_playlist = len(DATA.get_playlist_info())
    while True:
        try:
            user_input = int(input("Please choose a wanted playlist: "))
        except ValueError:
            print("A wanted playlist must be int")
        else:
            if 0 < user_input < nums_playlist + 1:
                return user_input
            print("Please choose existing playlist: ")



def main():
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
            read_wanted_playlist()
            DISPLAY.clear_screen()
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


if __name__ == "__main__":
    main()