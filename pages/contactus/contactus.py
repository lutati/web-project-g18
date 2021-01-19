from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# contactus blueprint definition
contactus = Blueprint('contactus', __name__, static_folder='static', static_url_path='/contactus',
                      template_folder='templates')


# Routes
@contactus.route('/contactus', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        affected_rows = dbManager.commit(
            "insert into contact_us(FullName, Email, Phone, comments) VALUES ('%s', '%s', '%s', '%s')" %
            (request.form['fullname'], request.form['email'],
             request.form['phone'], request.form['text_area']))
        print(affected_rows)

        return render_template('contactus.html')

    return render_template('contactus.html')

