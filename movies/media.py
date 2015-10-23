import webbrowser


class Movie():
    """Defines the movie data structure"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_lead, movie_imdb):
        """Initialize the movie object

        :param movie_title: Name of the movie
        :param movie_storyline: Short description of the movie
        :param poster_image: URL to an image of the movie's poster
        :param trailer_youtube: URL to a YouTube video of the movie's trailer
        :param movie_lead: Leading actor/actress
        :param movie_imdb: URL to the movie's IMDB page
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.leading_role = movie_lead
        self.imdb_url = movie_imdb
