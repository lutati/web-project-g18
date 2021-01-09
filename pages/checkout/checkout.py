from flask import Blueprint, render_template

# cart blueprint definition
checkout = Blueprint('checkout', __name__, static_folder='static', static_url_path='/checkout', template_folder='templates')


# Routes
@checkout.route('/checkout')
def index():
    return render_template('checkout.html')
