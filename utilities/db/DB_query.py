from utilities.db.db_manager import dbManager, DBManager


class DBQuery:

    def _init_(self):
        """
        Init dbmanager
        """
        self.db = DBManager()

    def get_product_vradim(self, product_name: str):
        self.db = DBManager()
        row = self.db.fetch('select * from products where Product_Name=%s',
                            (product_name,))
        return row

    def get_product_sahlav(self, product_name: str, product_type: str):
        self.db = DBManager()
        row = self.db.fetch('select * from products where Product_Name=%s and Dairy=%s',
                            (product_name, product_type))
        return row

    def get_product_malabi(self, product_type: str, malabi_syrup: str, malabi_topping: str):
        self.db = DBManager()
        row = self.db.fetch('select * from products where Dairy=%s and Syrup=%s and Topping=%s',
                            (product_type, malabi_syrup, malabi_topping))
        return row

    def user_data(self, uname: str, password: str):
        self.db = DBManager()
        row = self.db.fetch('select * from customers where Email=%s and User_Password=%s',
                            (uname, password))
        return row

    def get_max_order(self):
        self.db = DBManager()
        row = self.db.fetch('select (max(order_id)) as cartid from orders')
        row = row[0]
        return row

    def insert_contact_us(self, fname: str, email: str, phone: str, text_area: str):
        self.db = DBManager()
        row = self.db.commit(
            "insert into contact_us(FullName, Email, Phone, comments) VALUES ('%s', '%s', '%s', '%s')" %
            (fname, email, phone, text_area))
        return row

    def register_new_user(self, email: str, password: str, fname: str, lname: str, phone: str, date, gender: str):
        self.db = DBManager()
        row = self.db.commit(
            "insert into customers(Email, User_Password, First_Name, Last_Name, Phone, Birth_Date, Gender) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
            (email, password, fname, lname, phone, date, gender))
        return row

    def set_new_order(self, fname: str, email: str, phone: str, city: str, address: str, door: str, comments: str,
                      delivery: str, credit_card, cvv, made_by, all_total_quantity, all_total_price):
        self.db = DBManager()
        row = self.db.commit(
            "insert into orders(Full_Name, Email, Phone, City, Street, Apartment, Comments, Delivery_Option,  Credit_Card, cvv, made_by, total_quantity, amount_order) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
            (
                fname, email, phone, city, address, door, comments, delivery, credit_card, cvv, made_by,
                all_total_quantity,
                all_total_price))
        return row

    def update_customer(self, fname: str, lname: str, birthdate, phone, id):
        self.db = DBManager()
        row = self.db.commit(
            'update customers set  First_Name=%s, Last_Name=%s, Birth_Date=%s, Phone=%s where Email=%s',
            (fname, lname, birthdate, phone, id))
        return row

    def get_user(self, id):
        self.db = DBManager()
        row = self.db.fetch('select * from customers where Email=%s',
                            (id,))
        return row

    def delete_user(self, id):
        self.db = DBManager()
        row = self.db.commit(
            'delete from orders where made_by=%s',
            (id,))
        return row

    def delete_user_customer(self, id):
        self.db = DBManager()
        row = self.db.commit('delete from customers where Email=%s', (id,))
        return row

    def insert_into_products_orders(self, cart_table, max_order):
        self.db = DBManager()
        for key, value in cart_table.items():
            product_id = cart_table[key]['id']
            quantity = cart_table[key]['quantity']
            row = self.db.commit(
                "insert into products_in_order(order_id, product_id, quantity) VALUES ('%s', '%s', '%s')" % (
                    max_order, product_id, quantity))
        return row