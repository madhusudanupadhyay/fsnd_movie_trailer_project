"""
Movie model
"""

import webbrowser


class Movie(object):
    """ Defines movie model schema """

    def __init__(self, movie_title, movie_storyline,
                 movie_youtubeurl, movie_image):
        """ Assign supplied parameters to self instance """
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = movie_youtubeurl
        self.poster_image_url = movie_image

    def show_trailer(self):
        """ Open in the browser as Html """
        webbrowser.open(self.trailer_youtube_url)
