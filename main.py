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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name DATE NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unitary_value REAL NOT NULL,
    date DATE NOT NULL
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

while True:
    print('1 - List sales')
    print('2 - Insert sales')
    print('3 - Exit')
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
        break
    else:
        print('Invalid option')