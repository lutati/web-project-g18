from flask import Blueprint, render_template, request, redirect, url_for

from utilities.db.DB_query import DBQuery
from utilities.db.db_manager import dbManager

# cart blueprint definition
registration = Blueprint('registration', __name__, static_folder='static', static_url_path='/registration',
                         template_folder='templates')


# Routes
@registration.route('/registration', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = DBQuery()
        affected_rows = query.register_new_user(request.form['email'], request.form['password'],
                                                request.form['firstname'], request.form['lastname'],
                                                request.form['phone'], request.form['date'],
                                                request.form['gender'],
                                                )
        return redirect('/login')

    return render_template('registration.html')
