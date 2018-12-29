from flask import render_template
from app import app
from .request import get_movies, get_movie


# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    :return:
    '''

    # getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    print('\n\n\n#6#======================> START LOGGING popular_movies #####========================>\n\n\n')
    print(popular_movies)
    print('\n\n\n#6#======================> END LOGGING popular_movies #######========================>\n\n\n')
    # message = 'Hello World var'
    title = 'Home - Welcome to the Best Movie Review Website Online'
    return render_template('index.html', template_title_var = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

# dynamic routes
@app.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns the movie details and its data
    :param id:
    :return:
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title, movie = movie)