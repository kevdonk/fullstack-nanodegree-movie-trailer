class Movie():
    """ This class stores information about a movie """

    def __init__(self, release_date, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.date = release_date
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


