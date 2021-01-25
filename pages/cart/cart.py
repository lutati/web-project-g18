from flask import Blueprint, render_template, session
from utilities.db.db_manager import dbManager

# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():
    id = session['cart_number']
    print(id)
    # sum_product = dbManager.fetch('select sum(')
    cart_data = dbManager.fetch(
        'select cart_id,p.product_name, price, quantity from carts as c join products as p on c.product_id=p.Product_ID where c.cart_id=%s',
        (id,))
    print(cart_data)
    if cart_data:
        return render_template('cart.html', cart=cart_data)
    return render_template('cart.html')
