from flask import Blueprint, render_template, session, redirect, url_for, request

from utilities.db.db_manager import dbManager

# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():
    if 'cart_number' in session:
        id = session['cart_number']
        # sum_product = dbManager.fetch('select sum(')
        cart_data = dbManager.fetch(
            'select order_id, c.product_id, p.product_name, price, quantity from product_in_cart as c join products as p on c.product_id=p.Product_ID where c.order_id=%s',
            (id,))
        if cart_data:
            return render_template('cart.html', cart=cart_data)
    return render_template('cart.html')


@cart.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
    id_delete = request.form['hidden_id']
    if request.method == 'POST':
        basket_delete = dbManager.commit('DELETE FROM product_in_cart where product_id=%s',
                                         (id_delete,))
    return redirect(url_for('cart.index'))


@cart.route('/payment_item', methods=['GET', 'POST'])
def update_item():
    if request.method == 'GET':
        quantity = request.args.get('quantity')
