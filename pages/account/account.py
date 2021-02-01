from pages.products.products import *

# cart blueprint definition
account = Blueprint('account', __name__, static_folder='static', static_url_path='/account',
                    template_folder='templates')


# Routes
@account.route('/account')
def index():
    if 'logged_in' in session:
        query = DBQuery()
        user_details = query.get_user_details(session['email_user'])
        print(user_details)
    return render_template('/account.html', account=user_details)


@account.route('/update_details', methods=['GET', 'POST'])
def update_details():
    if request.method == 'POST':
        id = session['email_user']
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        birthdate = request.form['BD']
        phone = request.form['phone']
        query = DBQuery()
        row_update = query.update_customer(first_name, last_name, birthdate, phone, id)
        user = query.get_user(id)
        print(user)
        session['username'] = user[0].First_Name
        session['last_name'] = user[0].Last_Name
        session['phone'] = user[0].Phone
        session['birth_date'] = user[0].Birth_Date
        session['gender'] = user[0].Gender
        flash('הפרטים עודכנו בהצלחה !')
    return render_template('/account.html')


@account.route('/delete_details', methods=['GET', 'POST'])
def delete_details():
    if request.method == 'POST':
        id = session['email_user']
        query = DBQuery()
        delete_user = query.delete_user_orders(id)
        delete_user_customer = query.delete_user_customer(id)
        flash('עצובים להיפרד, לא מאוחר להירשם שוב :)')
        session.pop('logged_in', None)
        session.pop('username', None)
        session.pop('is_cart', False)
        session.pop('cart_number', None)
        session.pop('cart_array', None)
        return render_template('/login.html')


@account.route('/no_delete_details', methods=['GET', 'POST'])
def no_delete_details():
    if request.method == 'POST':
        flash('שמחים שהתחרטת ונשארת איתנו!')
    return render_template('/account.html')
