from flask import Blueprint, render_template, request, redirect, url_for
from utilities.db.db_manager import dbManager

# cart blueprint definition
registration = Blueprint('registration', __name__, static_folder='static', static_url_path='/registration',
                         template_folder='templates')


# Routes
@registration.route('/registration', methods=['GET', 'POST'])
def index():
    print('jjj')

    if request.method == 'POST':
        print('kkk')
        affected_rows = dbManager.commit(
            "insert into customers(Email, User_Password, First_Name, Last_Name, Phone, Birth_Date, Gender) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
            (request.form['email'], request.form['password'],
             request.form['firstname'], request.form['lastname'], request.form['phone'], request.form['date'],
             request.form['gender'],
             ))
        print(affected_rows)

        return redirect('/login')

    return render_template('registration.html')
