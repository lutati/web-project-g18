from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
# add some comments
###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## contactus
from pages.contactus.contactus import contactus
app.register_blueprint(contactus)

## checkout
from pages.checkout.checkout import checkout

app.register_blueprint(checkout)


## Aboutus
from pages.aboutus.aboutus import aboutus

app.register_blueprint(aboutus)

## cart
from pages.cart.cart import cart

app.register_blueprint(cart)

## events
from pages.events.events import events

app.register_blueprint(events)

## login
from pages.login.login import login
app.register_blueprint(login)

## products
from pages.products.products import products
app.register_blueprint(products)


## registration
from pages.registration.registration import registration
app.register_blueprint(registration)
#
# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)


###### Components
## Main menu


from components.header.header import header

app.register_blueprint(header)


from components.footer.footer import footer


app.register_blueprint(footer)


if __name__ == '__main__':
    app.run()
