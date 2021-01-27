from flask import Blueprint, render_template, session, redirect, url_for, request

from utilities.db.db_manager import dbManager

# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():
    id = session['cart_number']
    # sum_product = dbManager.fetch('select sum(')
    cart_data = dbManager.fetch(
        'select id, cart_id,p.product_name, price, quantity from carts as c join products as p on c.product_id=p.Product_ID where c.cart_id=%s',
        (id,))
    if cart_data:
        return render_template('cart.html', cart=cart_data)
    return render_template('cart.html')


@cart.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
    id_delete = request.form['hidden_id']
    if request.method == 'POST':
        basket_delete = dbManager.commit('DELETE FROM carts where id=%s', (id_delete,))
    return redirect(url_for('cart.index'))
