"""
Format array of movie models into html
"""

import webbrowser
import os

# Styles and scripting for the page
MAIN_PAGE_HEAD = u'''
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="A portfolio template that uses Material Design Lite.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <title>Maddy's Movie Box</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:regular,bold,italic,thin,light,bolditalic,black,medium&amp;lang=en">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.grey-pink.min.css" />
    <link rel="stylesheet" href="assets/styles.css" />

    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
'''

# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
        <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
            <div class="scale-media" id="trailer-video-container">
            </div>
        </div>
        </div>
    </div>
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header mdl-layout__header--waterfall portfolio-header">
            <div class="mdl-layout__header-row portfolio-logo-row">
                <span class="mdl-layout__title">
                    <div class="portfolio-logo"></div>
                    <span class="mdl-layout__title">Maddy's Movie Box</span>
                </span>
            </div>
            <div class="mdl-layout__header-row portfolio-navigation-row mdl-layout--large-screen-only">
                <nav class="mdl-navigation mdl-typography--body-1-force-preferred-font">
                    <a class="mdl-navigation__link is-active" href="index.html">Upcoming</a>
                </nav>
            </div>
        </header>
        <div class="mdl-layout__drawer mdl-layout--small-screen-only">
            <nav class="mdl-navigation mdl-typography--body-1-force-preferred-font">
                <a class="mdl-navigation__link is-active" href="index.html">Upcoming</a>
            </nav>
        </div>
        <main class="mdl-layout__content">
            <div class="mdl-grid portfolio-max-width">
                {movie_tiles}
            </div>
            <footer class="mdl-mini-footer">
                <div class="mdl-mini-footer__left-section">
                    <div class="mdl-logo">Maddy's Movie Box</div>
                </div>
            </footer>
        </main>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <script src="assets/main.js"></script>
</body>
</html>
'''

# A single movie entry html template
MOVIE_TITLE_CONTENT = '''
<div data-trailer-youtube-id="{trailer_youtube_id}" class="movie-tile mdl-cell mdl-card mdl-shadow--4dp portfolio-card">
    <div class="mdl-card__media">
        <img class="article-image" src="{poster_image_url}" border="0" alt="">
    </div>
    <div class="mdl-card__title">
        <h2 class="mdl-card__title-text">{movie_title}</h2>
    </div>
    <div class="mdl-card__supporting-text">
        {storyline}
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    """This is for holding the movie title"""
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += MOVIE_TITLE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.trailer_youtube_url,
            storyline=movie.storyline
        )
    return content


def open_movies_page(movies):
    """"This is needed to render our python movie function into an html"""
  # Create or overwrite the output file
    output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically
  # generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies))

  # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

  # open the output file in the browser
    url = os.path.abspath(output_file.name)
  # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)
