from flask import Blueprint, render_template, session, redirect, url_for, request
from utilities.db.db_manager import dbManager
from pages.products.products import *

# cart blueprint definition
account = Blueprint('account', __name__, static_folder='static', static_url_path='/account',
                    template_folder='templates')


# Routes
@account.route('/account')
def index():
    if 'logged_in' in session:
        user_details = dbManager.fetch('SELECT * from customers where Email=%s', (session['email_user'],))
        print(user_details)
    return render_template('/account.html', account=user_details)


@account.route('/update_details', methods=['GET', 'POST'])
def update_details():
    if request.method == 'POST':
        id = session['email_user']
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        birthdate = request.form['BD']
        phone = request.form['phone']

        row_affect = dbManager.commit(
            'update customers set  First_Name=%s, Last_Name=%s, Birth_Date=%s, Phone=%s where Email=%s',
            (first_name, last_name, birthdate, phone, id))

        user = dbManager.fetch('select * from customers where Email=%s',
                               (id,))
        print(user)
        session['username'] = user[0].First_Name
        session['last_name'] = user[0].Last_Name
        session['phone'] = user[0].Phone
        session['birth_date'] = user[0].Birth_Date
        session['gender'] = user[0].Gender
        flash('הפרטים עודכנו בהצלחה !')
    return render_template('/account.html')


@account.route('/delete_details', methods=['GET', 'POST'])
def delete_details():
    if request.method == 'POST':
        id = session['email_user']
        row_affect = dbManager.commit(
            'delete from orders where made_by=%s',
            (id,))
        row_affect_user = dbManager.commit('delete from customers where Email=%s', (id,))
        flash('עצובים להיפרד, לא מאוחר להירשם שוב :)')
        session.pop('logged_in', None)
        session.pop('username', None)
        session.pop('is_cart', False)
        session.pop('cart_number', None)
        session.pop('cart_array', None)
        return render_template('/login.html')


@account.route('/no_delete_details', methods=['GET', 'POST'])
def no_delete_details():
    if request.method == 'POST':
        flash('שמחים שהתחרטת ונשארת איתנו!')
    return render_template('/account.html')
