# import tkinter
from flask import Blueprint, render_template, request, session

from utilities.db.db_manager import dbManager
from utilities.db.DB_query import DBQuery
from flask import flash

products = Blueprint('products', __name__, static_folder='static', static_url_path='/products',
                     template_folder='templates')


# Routes
@products.route('/products')
def index():
    return render_template('products.html')


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False


def products_in_cart(row, new_quantity, item_array, all_total_quantity, all_total_price):
    if 'cart_array' in session:
        if str(row[0].Product_ID) in session['cart_array']:
            for key, value in session['cart_array'].items():
                if str(row[0].Product_ID) == key:
                    old_quantity = session['cart_array'][key]['quantity']
                    total_quantity = int(old_quantity) + int(new_quantity)
                    session['cart_array'][key]['quantity'] = total_quantity
                    session['cart_array'][key]['total_price'] = total_quantity * int(
                        session['cart_array'][key]['price'])
                    print('this is total price ###########################')
                    print(session['cart_array'][key]['total_price'])
                    flash("כמות הפריט נוספה בהתאם לבקשתך!")
        else:
            session['cart_array'] = array_merge(session['cart_array'], item_array)
            flash("הפריט נוסף בהצלחה לסל!")
        for key, value in session['cart_array'].items():
            individual_quantity = int(session['cart_array'][key]['quantity'])
            individual_price = int(session['cart_array'][key]['total_price'])
            all_total_quantity = all_total_quantity + individual_quantity
            all_total_price = all_total_price + individual_price
    else:
        session['cart_array'] = item_array
        all_total_quantity = all_total_quantity + int(new_quantity)
        all_total_price = all_total_price + int(new_quantity) * int(row[0].Price)
    session['all_total_quantity'] = all_total_quantity
    session['all_total_price'] = all_total_price


@products.route('/vradim', methods=['GET', 'POST'])
def products_in_orders():
    if 'logged_in' not in session:
        flash('שלום אורח! על מנת להזמין אנא הירשם תחילה, תודה')
        return render_template('products.html')
    if request.method == 'GET':
        print("bla")
        myproduct_name = "מי ורדים"
        row = dbManager.fetch('select * from products where Product_Name=%s',
                              (myproduct_name,))
        new_quantity = request.args.get('quantityV')
        total_price = int(row[0].Price) * int(new_quantity)
        print(row)
        item_array = {
            str(row[0].Product_ID): {'name': row[0].Product_Name, 'id': row[0].Product_ID,
                                     'price': row[0].Price, 'Dairy': row[0].Dairy, 'Syrup': row[0].Syrup,
                                     'topping': row[0].Topping, 'quantity': new_quantity, 'total_price': total_price}}
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True
        products_in_cart(row, new_quantity, item_array, all_total_quantity, all_total_price)
        return render_template('products.html')


@products.route('/sahlav', methods=['GET', 'POST'])
def products_sahlav():
    if 'logged_in' not in session:
        flash('שלום אורח! על מנת להזמין אנא הירשם תחילה, תודה')
        return render_template('products.html')
    if request.method == 'GET':
        x = DBQuery()
        myproduct_name = "סחלב"
        myproduct_type = request.args.get('type_sahlav')
        cart_id_int = session['cart_number']
        print(cart_id_int)
        new_quantity = request.args.get('quantityS')
        row = dbManager.fetch('select * from products where Product_Name=%s and Dairy=%s',
                              (myproduct_name, myproduct_type))
        total_price = int(row[0].Price) * int(new_quantity)
        item_array = {
            str(row[0].Product_ID): {'name': row[0].Product_Name, 'id': row[0].Product_ID,
                                     'price': row[0].Price, 'Dairy': row[0].Dairy, 'Syrup': row[0].Syrup,
                                     'topping': row[0].Topping, 'quantity': new_quantity, 'total_price': total_price}}
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True
        products_in_cart(row, new_quantity, item_array, all_total_quantity, all_total_price)
        return render_template('products.html')


@products.route('/malabi', methods=['GET', 'POST'])
def products_malabi():
    if 'logged_in' not in session:
        flash('שלום אורח! על מנת להזמין אנא הירשם תחילה, תודה')
        return render_template('products.html')
    if request.method == 'GET':
        myproduct_type = request.args.get('type_malabi')
        malabi_syrup = request.args.get('syrup')
        malabi_topping = request.args.get('toppings')

        new_quantity = request.args.get('quantity')
        row = dbManager.fetch('select * from products where Dairy=%s and Syrup=%s and Topping=%s',
                              (myproduct_type, malabi_syrup, malabi_topping))
        total_price = int(row[0].Price) * int(new_quantity)
        item_array = {
            str(row[0].Product_ID): {'name': row[0].Product_Name, 'id': row[0].Product_ID,
                                     'price': row[0].Price, 'Dairy': row[0].Dairy, 'Syrup': row[0].Syrup,
                                     'topping': row[0].Topping, 'quantity': new_quantity, 'total_price': total_price}}
        session.modified = True
        all_total_price = 0
        all_total_quantity = 0
        products_in_cart(row, new_quantity, item_array, all_total_quantity, all_total_price)
        return render_template('products.html')
