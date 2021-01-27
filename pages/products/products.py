import tkinter

from flask import Blueprint, render_template, request, session
from utilities.db.db_manager import dbManager
from tkinter import messagebox
# # This code is to hide the main tkinter window
# root = tkinter.Tk()
# root.withdraw()
# products blueprint definition
products = Blueprint('products', __name__, static_folder='static', static_url_path='/products',
                     template_folder='templates')


# Routes
@products.route('/products')
def index():
    return render_template('products.html')


@products.route('/vradim', methods=['GET', 'POST'])
def products_in_cart():
    if 'logged_in' not in session:
        messagebox.showinfo("Un Registered User", "אנא הירשמו תחילה כדי להנות מחוויה אישית :) תודה, מלביהו")
    if request.method == 'GET':

        print("bla")
        myproduct_name = "מי ורדים"
        myproduct_id = dbManager.fetch('select * from products where Product_Name=%s',
                                       (myproduct_name,))
        print(myproduct_id[0].Product_ID)
        myproduct_id_int = myproduct_id[0].Product_ID
        # price = 25.00
        cart_id_int = session['cart_number']
        new_quantity = request.args.get('quantityV')
        check_already_incart = dbManager.fetch(
            'select * from product_in_cart where order_id=%s and product_id=%s',
            (cart_id_int, myproduct_id_int))
        print(check_already_incart)
        if check_already_incart:
            print("if")
            update_quantity = dbManager.fetch(
                'select quantity from product_in_cart where order_id=%s and product_id=%s',
                (cart_id_int, myproduct_id_int))
            update_quantity = update_quantity[0].quantity
            update_quantity = int(update_quantity) + int(new_quantity)
            affect_rows_cart_sahlav = dbManager.commit(
                "UPDATE PRODUCT_IN_CART set quantity=%s where order_id=%s and product_id=%s",
                (update_quantity, cart_id_int, myproduct_id_int))
        else:
            print("else")

            affect_rows_cart_sahlav = dbManager.commit(
                "insert into product_in_cart(order_id, product_id, quantity) VALUES"
                " ('%s', '%s', '%s')" %
                (cart_id_int, myproduct_id_int, new_quantity))

        return render_template('products.html')


@products.route('/sahlav', methods=['GET', 'POST'])
def products_sahlav():
    if request.method == 'GET':
        myproduct_name = "סחלב"
        # print(request.args.get('type_sahlav'))
        myproduct_type = request.args.get('type_sahlav')
        myproduct_id = dbManager.fetch('select * from products where Dairy=%s',
                                       (myproduct_type,))
        # price = 15
        cart_id_int = session['cart_number']
        print(cart_id_int)
        new_quantity = request.args.get('quantityS')
        myproduct_id_int = myproduct_id[0].Product_ID
        check_already_incart = dbManager.fetch(
            'select * from product_in_cart where order_id=%s and product_id=%s',
            (cart_id_int, myproduct_id_int))
        print(check_already_incart)
        if check_already_incart:
            print("if")
            update_quantity = dbManager.fetch(
                'select quantity from product_in_cart where order_id=%s and product_id=%s',
                (cart_id_int, myproduct_id_int))
            update_quantity = update_quantity[0].quantity
            update_quantity = int(update_quantity) + int(new_quantity)
            affect_rows_cart_sahlav = dbManager.commit(
                "UPDATE PRODUCT_IN_CART set quantity=%s where order_id=%s and product_id=%s",
                (update_quantity, cart_id_int, myproduct_id_int))
        else:
            print("else")

            affect_rows_cart_sahlav = dbManager.commit(
                "insert into product_in_cart(order_id, product_id, quantity) VALUES"
                " ('%s', '%s', '%s')" %
                (cart_id_int, myproduct_id_int, new_quantity))
        return render_template('products.html')


@products.route('/malabi', methods=['GET', 'POST'])
def products_malabi():
    if request.method == 'GET':
        myproduct_name = "מלבי"
        myproduct_type = request.args.get('type_malabi')
        malabi_syrup = request.args.get('syrup')
        malabi_topping = request.args.get('toppings')
        malabi_product_id = dbManager.fetch('select * from products where Dairy=%s and Syrup=%s and Topping=%s',
                                            (myproduct_type, malabi_syrup, malabi_topping))
        print(malabi_product_id)
        # price = 10
        malabi_id_int = malabi_product_id[0].Product_ID
        cart_id_int = session['cart_number']
        new_quantity = request.args.get('quantity')
        check_already_incart = dbManager.fetch(
            'select * from product_in_cart where order_id=%s and product_id=%s',
            (cart_id_int, malabi_id_int))
        print(check_already_incart)
        if check_already_incart:
            print("if")
            update_quantity = dbManager.fetch(
                'select quantity from product_in_cart where order_id=%s and product_id=%s',
                (cart_id_int, malabi_id_int))
            update_quantity = update_quantity[0].quantity
            update_quantity = int(update_quantity) + int(new_quantity)
            affect_rows_cart_sahlav = dbManager.commit(
                "UPDATE PRODUCT_IN_CART set quantity=%s where order_id=%s and product_id=%s",
                (update_quantity, cart_id_int, malabi_id_int))
        else:
            print("else")

            affect_rows_cart_sahlav = dbManager.commit(
                "insert into product_in_cart(order_id, product_id, quantity) VALUES"
                " ('%s', '%s', '%s')" %
                (cart_id_int, malabi_id_int, new_quantity))

        return render_template('products.html')
