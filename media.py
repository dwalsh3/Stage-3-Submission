import webbrowser

class Movie():
    """This class provides a way to initialize movie variables (linking variable names with their
    corresponding movies), and a way to show movie trailers referencing only the name of the movie rather than the youtube URL."""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, ebert_quote):
        self.title               = movie_title
        self.storyline           = movie_storyline
        self.poster_image_url    = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ebert_quote		 = ebert_quote

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
