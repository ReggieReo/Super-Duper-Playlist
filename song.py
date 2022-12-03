class Song:

    def __init__(self, name: str, artist: str, duration: str,
                 language: str = "None", url: str = "None"):
        self.__name = name
        self.__artist = artist
        self.__duration = duration
        self.__language = language
        self.__url = url
        self.__rating = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name == "":
            raise TypeError("name must be string type variable")
        self.__name = new_name

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, new_artist):
        if not isinstance(new_artist, str) or new_artist == "":
            raise TypeError("artist must be string type variable")
        self.__artist = new_artist

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, str) or ":" not in new_duration:
            raise TypeError("duration of song must be string type")
        self.__duration = new_duration

    @property
    def language(self):
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
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if not isinstance(new_rating, float) or \
                new_rating < 0 or \
                new_rating > 5:
            raise TypeError("rating of song must be float type")
        self.__rating = new_rating
