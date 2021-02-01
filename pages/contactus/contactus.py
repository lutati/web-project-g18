from flask import Blueprint, render_template, request

from utilities.db.DB_query import DBQuery
from utilities.db.db_manager import dbManager

# contactus blueprint definition
contactus = Blueprint('contactus', __name__, static_folder='static', static_url_path='/contactus',
                      template_folder='templates')


# Routes
@contactus.route('/contactus', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = DBQuery()
        affect_row = query.insert_contact_us(request.form['fullname'], request.form['email'], request.form['phone'],
                                             request.form['text_area'])
        return render_template('contactus.html')

    return render_template('contactus.html')
