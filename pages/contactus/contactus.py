from flask import Blueprint, render_template

# cart blueprint definition
contactus = Blueprint('contactus', __name__, static_folder='static', static_url_path='/contactus', template_folder='templates')


# Routes
@contactus.route('/contactus')
def index():
    return render_template('contactus.html')
