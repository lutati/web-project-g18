from flask import Blueprint, render_template

# cart blueprint definition
registration = Blueprint('registration', __name__, static_folder='static', static_url_path='/registration', template_folder='templates')


# Routes
@registration.route('/registration')
def index():
    return render_template('registration.html')
