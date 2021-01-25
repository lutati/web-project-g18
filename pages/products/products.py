from flask import Blueprint, render_template, request, session
from utilities.db.db_manager import dbManager

# products blueprint definition
products = Blueprint('products', __name__, static_folder='static', static_url_path='/products',
                     template_folder='templates')


# Routes
@products.route('/products')
def index():
    return render_template('products.html')


@products.route('/vradim', methods=['GET', 'POST'])
def products_in_cart():
    if request.method == 'GET':
        print("bla")
        myproduct_name = "מי ורדים"
        myproduct_id = dbManager.fetch('select * from products where Product_Name=%s',
                                       (myproduct_name,))
        print(myproduct_id[0].Product_ID)
        myproduct_id_int = myproduct_id[0].Product_ID
        # price = 25.00
        cart_id_int = session['cart_number']
        Dairy = None
        Syrup = None
        affect_rows_cart = dbManager.commit(
            "insert into carts(cart_id, product_id, product_name, quantity) VALUES"
            " ('%s', '%s', '%s', '%s')" %
            (cart_id_int, myproduct_id_int, myproduct_name, 1))
        return render_template('products.html')


@products.route('/sahlav', methods=['GET', 'POST'])
def products_sahlav():
    if request.method == 'GET':
        myproduct_name = "סחלב"
        print(request.args.get('type_sahlav'))
        myproduct_type = request.args.get('type_sahlav')
        myproduct_id = dbManager.fetch('select * from products where Dairy=%s',
                                       (myproduct_type,))
        # price = 15
        cart_id_int = session['cart_number']
        print(cart_id_int)

        myproduct_id_int = myproduct_id[0].Product_ID
        affect_rows_cart_sahlav = dbManager.commit(
            "insert into carts(cart_id, product_id, product_name, quantity, product_type) VALUES"
            " ('%s', '%s', '%s', '%s', '%s')" %
            (cart_id_int, myproduct_id_int, myproduct_name, 1, myproduct_type))

        return render_template('products.html')


@products.route('/malabi', methods=['GET', 'POST'])
def products_malabi():
    if request.method == 'GET':
        myproduct_name = "מלבי"
        myproduct_type = request.args.get('type_malabi')
        malabi_syrup = request.args.get('syrup')
        malabi_product_id = dbManager.fetch('select * from products where Dairy=%s and Syrup=%s',
                                            (myproduct_type, malabi_syrup))
        print(malabi_product_id)
        # price = 10
        malabi_id_int = malabi_product_id[0].Product_ID
        cart_id_int = session['cart_number']
        toppings = [request.args.get('adds1'), request.args.get('adds2'), request.args.get('adds3'),
                    request.args.get('adds4')]
        print(toppings)
        affect_rows_cart_malabi = dbManager.commit(
            "insert into carts(cart_id, product_id, syrup, product_name, quantity, product_type) VALUES"
            " ('%s', '%s', '%s', '%s', '%s', '%s')" %
            (cart_id_int, malabi_id_int, malabi_syrup, myproduct_name, 1, myproduct_type))

        return render_template('products.html')
