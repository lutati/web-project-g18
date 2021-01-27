from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from flask import flash
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
            if 'is_cart' not in session:
                cart_id = dbManager.fetch('select (max(order_id)+1) as cartid from orders')
                affect_new_customer = dbManager.commit('INSERT INTO orders (order_id) values (%s)',
                                                       (cart_id[0].cartid,))
                print(cart_id)
                if affect_new_customer:
                    session['is_cart'] = True
                    session['cart_number'] = cart_id[0].cartid

            return render_template('homepage.html', user_session=session['username'],
                                   login_session=session['logged_in'])
        else:
            flash("שם משתמש או סיסמא אינם נכונים")
    return render_template('login.html')
