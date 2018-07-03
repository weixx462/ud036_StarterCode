import webbrowser


class Movie():
    """The Movie class to construct movie instances

    Attributes:
        movie_title (str): the title of movie.
        movie_storyline (str): the storyline of movie.
        poster_image (str): url of movie poster image.
        trailer_youtube (str): url of movie trailer.

    """
    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
