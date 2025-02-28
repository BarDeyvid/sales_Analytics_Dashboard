import sqlite3
#import matplotlib.pyplot as plt
import os

def clear():
    """
    Clears the terminal screen.

    Uses the 'cls' command for Windows and 'clear' command for Unix-based systems.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

conn = sqlite3.connect('data/db.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    salesperson_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    sale_amount DECIMAL(10,2) NOT NULL,
    quantity_sold INTEGER NOT NULL,
    discount DECIMAL(5,2) NOT NULL,
    region_id INTEGER NOT NULL,
    payment_method VARCHAR(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(100) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    customer_address VARCHAR(200) NOT NULL,
    customer_type VARCHAR(50) NOT NULL,
    customer_since DATE NOT NULL,
    region_id INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(100) NOT NULL,
    product_description TEXT NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL,
    product_cost DECIMAL(10,2) NOT NULL,
    product_stock INTEGER NOT NULL,
    product_launch_date DATE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS salespersons (
    salesperson_id INTEGER PRIMARY KEY AUTOINCREMENT,
    salesperson_name VARCHAR(100) NOT NULL,
    salesperson_email VARCHAR(100) NOT NULL,
    salesperson_phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    region_id INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_name VARCHAR(100) NOT NULL,
    region_manager VARCHAR(100) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS time_periods (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    day_of_week VARCHAR(20) NOT NULL,
    week_of_year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    year INTEGER NOT NULL,
    is_weekend BOOLEAN NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS discounts (
    discount_id INTEGER PRIMARY KEY AUTOINCREMENT,
    discount_name VARCHAR(100) NOT NULL,
    discount_percentage DECIMAL(5,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    active BOOLEAN NOT NULL
)
''')

def insert_sales():
    """
    Insert a new sales record into the database.

    Prompts the user to enter various pieces of information about the sale,
    and then inserts this information into the database.
    """
    name = input('Name: ')
    age = int(input('Age: '))
    city = input('City: ')
    product = input('Product: ')
    quantity = int(input('Quantity: '))
    unitary_value = float(input('Unitary value: '))
    date = input('Date: ')
    cursor.execute('''
            INSERT INTO sales (name, age, city, product, quantity, unitary_value, date)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (name, age, city, product, quantity, unitary_value, date))
    conn.commit()
    clear()
    print('Sale inserted successfully')
def insert_customers():
    '''
    Insert a new customer record into the database.

    Prompts the user to enter various pieces of information about the customer,'''
    costumer_name = input('Costumer Name: ')
    costumer_email = input('Costumer Email: ')
    costumer_phone = input('Costumer Phone: ')
    costumer_address = input('Costumer Address: ')
    costumer_type = input('Costumer Type: ')
    costumer_since = input('Costumer Since: ')
    region_id = int(input('Region ID: '))
    cursor.execute('''
            INSERT INTO customers (costumer_name, costumer_email, costumer_phone, costumer_address, costumer_type, costumer_since, region_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (costumer_name, costumer_email, costumer_phone, costumer_address, costumer_type, costumer_since, region_id))
    conn.commit()
    clear()
    print('Customer inserted successfully')

def insert_products():
    '''
    Insert a new product record into the database.

    Prompts the user to enter various pieces of information about the product,'''
    product_name = input('Product Name: ')
    product_description = input('Product Description: ')
    product_category = input('Product Category: ')
    product_price = float(input('Product Price: '))
    product_cost = float(input('Product Cost: '))
    product_stock = int(input('Product Stock: '))
    product_launch_date = input('Product Launch Date: ')
    cursor.execute('''
                   INSERT INTO products (product_name, product_description, product_category, product_price, product_cost, product_stock, product_launch_date)
                   values (?, ?, ?, ?, ?, ?, ?)''',
                   (product_name, product_description, product_category, product_price, product_cost, product_stock, product_launch_date))
    conn.commit()
    clear()
    print('Product inserted successfully')

def insert_salespersons():
    '''
    Insert a new salesperson record into the database.

    Prompts the user to enter various pieces of information about the salesperson,'''
    salesperson_name = input('Salesperson Name: ')
    salesperson_email = input('Salesperson Email: ')
    salesperson_phone = input('Salesperson Phone: ')
    hire_date = input('Hire Date: ')
    region_id = int(input('Region ID: '))
    cursor.execute('''
                   INSERT INTO salespersons (salesperson_name, salesperson_email, salesperson_phone, hire_date, region_id)
                   values (?, ?, ?, ?, ?)''',
                   (salesperson_name, salesperson_email, salesperson_phone, hire_date, region_id))
    conn.commit()
    clear()
    print('Salesperson inserted successfully')

def insert_time_periods():
    '''
    Insert a new time period record into the database.

    Prompts the user to enter various pieces of information about the time period,'''
    date = input('Date: ')
    day_of_week = input('Day of Week: ')
    week_of_year = int(input('Week of Year: '))
    month = int(input('Month: '))
    quarter = int(input('Quarter: '))
    year = int(input('Year: '))
    is_weekend = input('Is Weekend: ')
    cursor.execute('''
                   INSERT INTO time_periods (date, day_of_week, week_of_year, month, quarter, year, is_weekend)
                   values (?, ?, ?, ?, ?, ?, ?)''',
                   (date, day_of_week, week_of_year, month, quarter, year, is_weekend))
    conn.commit()
    clear()
    print('Time period inserted successfully')

def insert_regions():
    '''
    Insert a new region record into the database.

    Prompts the user to enter various pieces of information about the region,'''
    region_name = input('Region Name: ')
    region_manager = input('Region Manager: ')
    cursor.execute('''
                   INSERT INTO regions (region_name, region_manager),
                   values (?, ?)''',
                   (region_name, region_manager))
    conn.commit()
    clear()
    print('Region inserted successfully')

def insert_discounts():
    '''
    Insert a new discount record into the database.'''
    discount_name = input('Discount Name: ')
    discount_percentage = float(input('Discount Percentage: '))
    start_date = input('Start Date: ')
    end_date = input('End Date: ')
    active = input('Active: ')
    cursor.execute('''
                   INSERT INTO discounts (discount_name, discount_percentage, start_date, end_date, active)
                   values (?, ?, ?, ?, ?)''',
                   (discount_name, discount_percentage, start_date, end_date, active))
    conn.commit()
    clear()
    print('Discount inserted successfully')

def option_one():
# List All Sales in the Database
    print('1 - List sales')
    print('2 - Insert sales')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM sales')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_sales()
        clear()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_two():
    ''' Customers'''
    print('1 - List customers')
    print('2 - Insert customers')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM customers')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_customers()
        clear()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_three():
    ''' Products '''
    print('1 - List products')
    print('2 - Insert products')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM products')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_products()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_four():
    print('1 - List salespersons')
    print('2 - Insert salespersons')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM salespersons')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_salespersons()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_five():
    print('1 - List regions')
    print('2 - Insert regions')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM regions')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_regions()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_six():
    print('1 - List time periods')
    print('2 - Insert time periods')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM time_periods')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_time_periods()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_seven():
    print('1 - List discounts')
    print('2 - Insert discounts')
    print('3 - Return to main menu')
    option = int(input('Option: '))
    if option == 1:
        cursor.execute('SELECT * FROM discounts')
        for row in cursor.fetchall():
            print(row)
    elif option == 2:
        insert_discounts()
    elif option == 3:
        clear()
        return
    else:
        print('Invalid option')

def option_eight():
    conn.close()
    exit()

options = {
    1: option_one,
    2: option_two,
    3: option_three,
    4: option_four,
    5: option_five,
    6: option_six,
    7: option_seven,
    8: option_eight
}

while True:
    print('Sales Management System')
    print('-----------------------')
    print('Options:')
    print('1 - Sales')
    print('2 - Customers')
    print('3 - Products')
    print('4 - Salespersons')
    print('5 - Regions')
    print('6 - Time periods')
    print('7 - Discounts')
    print('8 - Exit')
    
    choice = input('Option: ')
    
    try:
        choice = int(choice)
        options.get(choice, lambda: print('Invalid option'))()
    except Exception as e:
        print('Invalid option')
        print(e)
        continue