from flask import Blueprint, render_template, request, session, url_for, redirect, flash

# cart blueprint definition
from utilities.db.db_manager import dbManager

login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uname = request.form['email']
        password = request.form['password']
        user = dbManager.fetch('select * from customers where Email=%s and User_Password=%s',
                               (uname, password))

        if user and len(user):
            session['logged_in'] = True
            session['username'] = user[0].First_Name

            return render_template('homepage.html', user_session=session['username'],
                                   login_session=session['logged_in'])
    return render_template('login.html')
