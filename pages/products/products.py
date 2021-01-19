from flask import Blueprint, render_template, request, session

# products blueprint definition
products = Blueprint('products', __name__, static_folder='static', static_url_path='/products', template_folder='templates')


# Routes
@products.route('/products')
def index():
    return render_template('products.html')


@products.route('/products_in_cart', methods=['GET', 'POST'])
def products_in_cart():
    if request.method == 'POST':
        print(request.form['product2'])
    # id = session['']
    # type_malabi = request.form['type_malabi']
    # syrup = request.form['syrup']
    # if (request.form['vradim_25']):
    #    price = '25'
    # if (request.form['sahlav_15']):
    #    price = '25'