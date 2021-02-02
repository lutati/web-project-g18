from flask import Blueprint, render_template, request, session, flash

from utilities.db.DB_query import DBQuery
from utilities.db.db_manager import dbManager

# cart blueprint definition
checkout = Blueprint('checkout', __name__, static_folder='static', static_url_path='/checkout',
                     template_folder='templates')


# Routes
@checkout.route('/checkout')
def index():
    id = session['cart_number']

    return render_template('checkout.html')


@checkout.route('/order', methods=['GET', 'POST'])
def order_customer():
    if request.method == 'POST':
        full_name = request.form['name']
        city = request.form['city']
        address = request.form['address']
        door = request.form['door']
        email = request.form['email']
        phone = request.form['tel']
        comments = request.form['comments']
        delivery = request.form['delivery']
        card_number = request.form['card_num']
        cvv = request.form['CVV']
        print(delivery)
        query = DBQuery()
        affect_row = query.set_new_order(full_name, email, phone, city, address, door, comments, delivery, card_number,
                                         cvv,
                                         session['email_user'],
                                         (session['all_total_quantity']),
                                         (session['all_total_price']))

        flash('תודה על קנייתך! מוזמן גם להעיף מבט על מגוון אירועים שלנו!')
        return render_template('events.html')
