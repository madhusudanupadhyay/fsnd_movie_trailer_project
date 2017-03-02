"""
    Render movies using tmdb API
"""
import fresh_tomatoes
import movie
import requests

BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = 'a6858133c502c06591520aeea294f20b'

UPCOMING_URL = '%s/movie/upcoming?api_key=%s' % (BASE_URL, API_KEY)

def movie_details_url(movie_id):
    """ Returns API url for getting movie details """
    return '%s/movie/%s?api_key=%s&append_to_response=videos' % (BASE_URL, movie_id, API_KEY)

def upcoming_movie_ids():
    """ Get upcoming movie ids from the API """
    response = requests.get(UPCOMING_URL).json()
    movies = response['results']
    ids = [movie_obj['id'] for movie_obj in movies]
    return ids

def get_movie_model(api_url):
    """ Make movie model from url """
    res = requests.get(api_url).json()
    title = res['title'].encode('ascii', 'ignore')
    storyline = res['overview'].encode('ascii', 'ignore')
    yt_code = res['videos']['results'][0]['key'].encode('ascii', 'ignore')
    poster = 'https://image.tmdb.org/t/p/w500/' + res['poster_path'].encode('ascii', 'ignore')

    return movie.Movie(title, storyline, yt_code, poster)


def upcoming_movies():
    """ Get array of upcoming movies """
    movie_ids = upcoming_movie_ids()
    urls = [movie_details_url(movie_id) for movie_id in movie_ids]

    return [get_movie_model(api_url) for api_url in urls]

# Opening web browser to show movies page
fresh_tomatoes.open_movies_page(upcoming_movies())
