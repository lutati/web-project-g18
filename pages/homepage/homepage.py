from flask import Blueprint, render_template, redirect, url_for, session
from utilities.db.db_manager import dbManager

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage',
                     template_folder='templates')


# Routes
@homepage.route('/')
def index():

    return render_template('homepage.html')
