from flask import Blueprint, render_template, request, session
from utilities.db.db_manager import dbManager

# cart blueprint definition
checkout = Blueprint('checkout', __name__, static_folder='static', static_url_path='/checkout',
                     template_folder='templates')


# Routes
@checkout.route('/checkout')
def index():
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
        fname_card = request.form['fname_card']
        id_customer = request.form['id_num']
        card_number = request.form['card_num']
        month = request.form['month']
        cvv = request.form['CVV']
        affect_rows = dbManager.commit(
            "insert into orders(Full_Name, Email, Phone, City, Street, Apartment, Comments, Delivery_Option) VALUES"
            " ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            full_name, email, phone, city, address, door, comments, delivery))

        myproduct_id_int = myproduct_id[0].Product_ID
        affect_rows_cart_sahlav = dbManager.commit(
            "insert into carts(cart_id, product_id, product_name, quantity, product_type) VALUES"
            " ('%s', '%s', '%s', '%s', '%s')" %
            (cart_id_int, myproduct_id_int, myproduct_name, 1, myproduct_type))

        return render_template('products.html')
