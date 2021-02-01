from flask import Blueprint, render_template, url_for, session

# main_menu blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')


@header.route('/logout', methods=['GET', 'POST'])
def logout_func():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('is_cart', False)
    session.pop('cart_number', None)
    session.pop('cart_array', None)

    return render_template('/homepage.html')
