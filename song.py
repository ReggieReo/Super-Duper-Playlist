class Song:
    """
        This class contains all of a song's information that will pass on
    and be used in the playlist class.
    """

    def __init__(self, name: str, artist: str, language: str = "None",
                 url: str = "None"):
        """
        Attribute of a song class.

        name: the name of the song.
        artist: the artist that wrote the song.
        language: the language, which the song is written in.
        url: the YouTube or other music provider url of the song.
        rating: the rating out of 5 of the song.
        """
        self.__name = name
        self.__artist = artist
        self.__language = language
        self.__url = url
        self.__rating = 0

    @property
    def name(self):
        """
        Getter and setter of the attribute name.
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name == "":
            raise TypeError("name must be string type variable")
        self.__name = new_name

    @property
    def artist(self):
        """
        Getter and setter of the attribute artist.
        """
        return self.__artist

    @artist.setter
    def artist(self, new_artist):
        if not isinstance(new_artist, str) or new_artist == "":
            raise TypeError("artist must be string type variable")
        self.__artist = new_artist

    @property
    def language(self):
        """
        Getter and setter of the attribute language.
        """
        return self.__language

    @language.setter
    def language(self, new_language):
        if not isinstance(new_language, str):
            raise TypeError("language of song must be string type")
        if new_language == "":
            new_language = "None"
        self.__language = new_language

    @property
    def url(self):
        """
        Getter and setter of the attribute url.
        """
        return self.__url

    @url.setter
    def url(self, new_url):
        if not isinstance(new_url, str) or "https" not in new_url:
            raise TypeError("url of song must be string type")
        if new_url == "":
            new_url = "None"
        self.__url = new_url

    @property
    def rating(self):
        """
        Getter and setter of the attribute rating.
        """
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if not isinstance(new_rating, (float, int)) or \
                new_rating < 0 or \
                new_rating > 5:
            raise TypeError("rating of song must be float or integer type")
        self.__rating = int(new_rating)
