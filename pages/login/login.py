from flask import Blueprint, render_template, request, session, url_for, redirect, flash
import mysql.connector

# cart blueprint definition
from utilities.db.db_manager import dbManager

login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# def interact_db(query, query_type: str):
#     return_value = False
#     connection = mysql.connector.connect(host='localhost',
#                                          user='root',
#                                          password='root',
#                                          database='webprojectg18')
#     cursor = connection.cursor(named_tuple=True)
#     cursor.execute(query)

    # if query_type == 'commit':
    #     # changes in db= commit
    #     connection.commit()
    #     return_value = True

    # if query_type == 'fetch':
    #     # take all data that sumnu. list of uesrs
    #     query_result = cursor.fetchall()
    #     return_value = query_result

    # connection.close()
    # cursor.close()
    # return return_value


# Routes
@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uname = request.form['email']
        password = request.form['password']
        print(password)

        user = dbManager.fetch('select * from customers where Email=%s and Password=%s'), (uname, password)
        print(user)

        user_data = dbManager.fetch('select * from customers  where Email=%s', (uname,))
        if user and len(user):
            session['logged_in'] = True
            session['user_data'] = {
                'first_name': user_data[0].Full_Name,
                'E_mail': user_data[0].Email,
                'phone': user_data[0].Phone,
                'birth': user_data[0].Birth_Date,
                'gender': user_data[0].Gender,
                'user_password': user_data[0].User_Password,
            }
            return redirect(url_for('my_account.index'))
        else:
            flash(u'Invalid password provided', 'error')
    return render_template('login.html')
