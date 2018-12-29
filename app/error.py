from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    function o render the 404 error page
    :param error:
    :return:
    '''
    return render_template('fourOwfour.html'),404