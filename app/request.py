from app import app
import urllib.request, json
from .models import movie

Movie = movie.Movie

# getting api key
api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]


def get_movies(category):
    '''
    function that gets the json response to our url request
    :param category:
    :return:
    '''

    get_movies_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)
            print('\n\n\n#1#======================> START LOGGING movie_results_list ========================>\n\n\n')
            print(movie_results_list)
            print('\n\n\n#1#======================> END LOGGING movie_results_list ##========================>\n\n\n')
            print('\n\n\n#2#======================> START LOGGING movie_results #####========================>\n\n\n')
            print(movie_results)
            print('\n\n\n#2#======================> END LOGGING movie_results #######========================>\n\n\n')
    return movie_results


def process_results(movie_list):
    '''
    Function that processes the movie result and transform them into list of objects

    Args:
        movie_list: a list of dictionaries that contain movie details

    Returns:
        movie_results; a list of movie objects
    :param movie_list:
    :return:
    '''

    print('\n\n\n#3#========================> START LOGGING movie_list #####========================>\n\n\n')
    print(movie_list)
    print('\n\n\n#3#========================> END LOGGING movie_list #######========================>\n\n\n')
    proc_movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            proc_movie_results.append(movie_object)
    return proc_movie_results
