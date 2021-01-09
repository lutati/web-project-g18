from flask import Blueprint, render_template

# cart blueprint definition
aboutus = Blueprint('aboutus', __name__, static_folder='static', static_url_path='/aboutus', template_folder='templates')


# Routes
@aboutus.route('/aboutus')
def index():
    return render_template('aboutus.html')
