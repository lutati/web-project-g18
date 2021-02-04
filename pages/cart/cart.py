from flask import Blueprint, render_template, session, redirect, url_for, request
from utilities.db.db_manager import dbManager
from pages.products.products import *
# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():

    if 'logged_in' in session:
        if 'cart_array' in session:
            return render_template('cart.html', item=session['cart_array'])
        return render_template('cart.html', item=False)
    return render_template('cart.html')


@cart.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
    all_total_price = 0
    all_total_quantity = 0
    session.modified = True
    id_delete = request.form['hidden_id']
    for item in session['cart_array'].items():
        if item[0] == id_delete:
            session['cart_array'].pop(item[0], None)
            if 'cart_array' in session:
                for key, value in session['cart_array'].items():
                    individual_quantity = int(session['cart_array'][key]['quantity'])
                    individual_price = int(session['cart_array'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            break
    session['all_total_quantity'] = all_total_quantity
    session['all_total_price'] = all_total_price
    return redirect(url_for('cart.index'))