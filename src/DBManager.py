import sqlite3
from operator import itemgetter
__author__ = 'casey & kevin'

class DBManager():

    def __init__(self):
        db = sqlite3.connect("band_database")
        cur = db.cursor()

        self.db = db
        self.cur = cur
    # Handles access to the database

    # this is where the database starts up. It will create the four tables that are needed.
    def startup_database(self):

        self.cur.execute('drop table if exists merchandise')
        self.cur.execute('drop table if exists sales')
        self.cur.execute('drop table if exists line_item_sales')
        self.cur.execute('drop table if exists tour_schedule')

        self.cur.execute('create table if not exists merchandise (merch_id int, merch_name text, sales_price real, unit_price real, inventory int, total_sold int)')
        self.cur.execute('create table if not exists sales(sale_id int, tour_id int, items_sold int, total_sales_price real, total_unit_price real)')
        self.cur.execute('create table if not exists line_item_sales(sale_id int, sale_line_item_id int, merch_id int, sales_price real, unit_price real)')
        self.cur.execute('create table if not exists tour_schedule(tour_id int, street_address text, city text, state text, zip int, tour_date blob, capacity int, cover_charge real, door_pay real, tickets_sold int)')

    # adds the test data.
    def add_test_data(self):
        merch_test_data = [(1, "first album", 14.99, 5.00, 300, 20),
                           (2, "second album", 14.99, 4.00, 500, 100),
                           (3, "band_hoodie", 30.00, 10.00, 100, 10),
                           (4, "band_patch", 5.00, 1.00, 50, 50),
                           (5, "band_hat", 17.00, 3.00, 20, 3)]

        sales_test_data = [(1, 1, 2, 35.00, 11.00),
                           (2, 1, 2, 29.98, 9.00),
                           (3, 2, 1, 17.00, 3.00)]

        line_item_test_data = [(1, 1, 3, 30.00, 10.00),
                               (1, 2, 4, 5.00, 1.00),
                               (2, 3, 2, 14.99, 4.00),
                               (2, 4, 1, 14.99, 5.00),
                               (3, 5, 5, 17.00, 3.00)]

        tour_table_test_data = [(1, "701 First Ave N", "Minneapolis", "MN", 55403, "1-20-16", 1500, 20.00, 10.00, 800),
                                (2, "621 Main Ave", "Fargo", "ND", 58102, "1-24-16", 500, 10.00, 5.00, 300),
                                (3, "410 Something Street", "Rapid City", "IA", 11223, "1-27-16", 800, 10.00, 5.00, 400),
                                (4, "1122 Street", "Madison", "WI", 45680, "2-5-16", 900, 10.00, 4.00, 200),
                                (5, "5th Street", "Chicago", "IL", 86753, "2-14-16", 1200, 12.00, 6.00, 600)]

        self.cur.executemany('insert into merchandise values (?, ?, ?, ?, ?, ?)', merch_test_data)
        self.cur.executemany('insert into sales values (?, ?, ?, ?, ?)', sales_test_data)
        self.cur.executemany('insert into line_item_sales values (?, ?, ?, ?, ?)', line_item_test_data)
        self.cur.executemany('insert into tour_schedule values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tour_table_test_data)

    # This create a new line of merchandise in the merchandise database.
    def add_new_merchandise(self, name, sale_price, unit_price, amount):
        try:
            key_id = self.get_next_id("merchandise")
            self.cur.execute('insert into merchandise values (?, ?, ?, ?, ?, ?)', [key_id, name, sale_price, unit_price, amount, 0])
            return True
        except Exception:
            return False

    # This adds a new sale to the tables. It does so by first creating the necessary number of line items
    # (individual products come in as a list). It then uses these to to build the individual sales list.
    # Finally it reduces the  number from the merchandise by an appropriate amount.
    def add_new_sale(self, units_sold_id_list, tour_id):
        try:

            sales_key = self.get_next_id("sales")
            total_sales = 0
            total_cost = 0
            total_sales_count = 0

            for merch_key in units_sold_id_list:
                merch_key_tuple = (merch_key, )
                merch_sales_price = self.cur.execute('select sales_price from merchandise where merch_id = ?', merch_key_tuple)
                merch_unit_price = self.cur.execute('select unit_id from merchandise where merch_id = ?', merch_key_tuple)
                self.create_line_item(sales_key, merch_key, merch_sales_price, merch_unit_price)

                total_items_sold = self.cur.execute('select total_sold from merchandise where merch_id = ?', merch_key_tuple)
                total_items_sold += 1
                merch_total = self.cur.execute('select inventory from merchandise where merch_id = ?', merch_key_tuple)
                merch_total -= 1
                self.cur.execute('update merchandise set inventory = ?, total_sold = ? where merch_id ?', [merch_total, total_items_sold, merch_key])

                total_sales += merch_sales_price
                total_cost += merch_unit_price
                total_sales_count += 1

            self.cur.execute('insert into sales values (?, ?, ?, ?, ?)', [sales_key, tour_id, total_sales_count, total_sales, total_cost])
            return True

        except Exception:
            return False

    def add_new_tour_date(self, street_address, city, state, zip, tour_date, capacity, cover_charge, door_charge):
        tour_id = self.get_next_id("tour_schedule")
        self.cur.execute('insert into tour_schedule values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         [tour_id, street_address, city, state, zip, tour_date, capacity,
                          cover_charge, door_charge, 0])

    # this closes the database.
    def close_database(self):
        self.db.close()

    # this creates a new line item.
    def create_line_item(self, sales_key, merch_key, merch_sales_price, merch_unit_price):
        line_item_key = self.get_next_id("line_item_sales")
        self.cur.execute('insert into line_item_sales values (?, ?, ?, ?, ?)',
                         [line_item_key, sales_key, merch_key, merch_sales_price, merch_unit_price])

    # This collects information from the merchandise table.
    def get_table_data(self, table_name):
        self.cur.execute('select * from ' + table_name)
        return_list = []
        for row in self.cur:
            return_list.append(row)
        return return_list

    # this gets the next available id for a given table.
    def get_next_id(self, table_name):
        new_id = 1
        self.cur.execute("SELECT * FROM " + table_name)
        for row in self.cur:
            new_id += 1
        return new_id

    def show_all(self):
        self.cur.execute('select * from merchandise')
        for row in self.cur:
            print(row)
        self.cur.execute('select * from sales')
        for row in self.cur:
            print(row)
        self.cur.execute('select * from line_item_sales')
        for row in self.cur:
            print(row)
        self.cur.execute('select * from tour_schedule')
        for row in self.cur:
            print(row)

    def show_best_units_sold(self):
        self.cur.execute('select * from merchandise')
        best_selling_list = []
        for item in self.cur:
            best_selling_list.append(item)

        # procedure taken from StackOverFlow: http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
        best_selling_list = sorted(best_selling_list, key=lambda tup:tup[5], reverse= True)

        print("Ordered by Best Selling")
        for item in best_selling_list:
            print(item[2])

    # this function takes the number of items sold for each unit, multiplies by the sales_price of each unit, and...
    # then sorts by the gross value of the sales.
    def show_best_units_sold_gross(self):
        self.cur.execute('select * from merchandise')
        gross_list = []

        for item in self.cur:
            units_sold = item[5]
            sales_price = item [2]
            total_sales = units_sold * sales_price
            new_item = (item, total_sales)
            gross_list.append(new_item)

        # procedure taken from StackOverFlow: http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
        gross_list = sorted(gross_list, key=lambda tup:tup[1], reverse= True)

        for item in gross_list:
            print(item)

    #this function shows the net value of each item sold, and then reports it back.
    def show_best_units_sold_net(self):
        self.cur.execute('select * from merchandise')
        gross_list = []

        for item in self.cur:
            units_sold = item[5]
            sales_price = item[2]
            unit_cost = item[3]
            net_sales = (units_sold * sales_price) - (units_sold * unit_cost)
            new_item = (item, net_sales)
            gross_list.append(new_item)

        # procedure taken from StackOverFlow: http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
        gross_list = sorted(gross_list, key=lambda tup:tup[1], reverse= True)

        for item in gross_list:
            print(item)

    def show_line_item_sales(self):
        self.cur.execute('select * from line_item_sales')
        for row in self.cur:
            print(row)
        return self.cur

    def show_merchandise(self):
        self.cur.execute('select * from merchandise')
        for row in self.cur:
            print(row)
        return self.cur

    def show_sales(self):
        self.cur.execute('select * from sales')
        for row in self.cur:
            print(row)
        return self.cur

    def show_tour_schedule(self):
        self.cur.execute('select * from tour_schedule')
        for row in self.cur:
            print(row)
        return self.cur