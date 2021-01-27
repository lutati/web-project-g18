from flask import Blueprint, render_template, redirect, url_for, session
from utilities.db.db_manager import dbManager

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage',
                     template_folder='templates')


# Routes
@homepage.route('/')
def index():
    if 'is_cart' not in session:
        cart_id = dbManager.fetch('select (max(cart_id)+1) as cartid from carts')
        row_affected = dbManager.commit('INSERT INTO CARTS (cart_id) values (%s)', (cart_id[0].cartid,))
        print(cart_id)
        if row_affected:
            session['is_cart'] = True
            session['cart_number'] = cart_id[0].cartid

    return render_template('homepage.html')

