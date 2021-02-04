from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from flask import flash
# cart blueprint definition
from utilities.db.DB_query import DBQuery
from utilities.db.db_manager import dbManager

login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uname = request.form['email']
        password = request.form['password']
        query = DBQuery()
        user = query.user_data(uname, password)
        if user and len(user):
            session['logged_in'] = True
            session['username'] = user[0].First_Name
            session['email_user'] = user[0].Email
            session['last_name'] = user[0].Last_Name
            session['phone'] = user[0].Phone
            session['birth_date'] = user[0].Birth_Date
            session['gender'] = user[0].Gender
            print(session['email_user'])
            if 'is_cart' not in session:
                session['is_cart'] = True

            return render_template('homepage.html', user_session=session['username'],
                                   login_session=session['logged_in'])
        else:
            flash("שם משתמש או סיסמא אינם נכונים")
    return render_template('login.html')