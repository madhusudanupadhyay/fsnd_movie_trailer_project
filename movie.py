import webbrowser

class Movie():
    """ Just trying to see what Documentation is like """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, movie_youtubeurl, movie_image):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = movie_youtubeurl
        self.poster_image_url = movie_image
    def show_trailer(self):
        """Open in the browser as Html"""
        webbrowser.open(self.trailer_youtube_url)


