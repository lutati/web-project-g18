from flask import Blueprint, render_template

# about blueprint definition
events= Blueprint('events', __name__, static_folder='static', static_url_path='/events', template_folder='templates')


# Routes
@events.route('/events')
def index():
    return render_template('events.html')
