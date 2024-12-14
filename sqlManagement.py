import sqlite3
import os

# Database Operations
def create_items_table():
    """Creates the student table if it doesn't exist."""
    conn = sqlite3.connect('z_resters.db')
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INT (11) PRIMARY KEY,
            item_type TEXT,
            item_name TEXT,
            price DECIMAL (8, 2) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_receipts_table():
    """Creates the student table if it doesn't exist."""
    conn = sqlite3.connect('z_resters.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            order_id INT (11) PRIMARY KEY,
            table_number INT (2),
            emp_id INT (11),
            date TEXT,
            time TEXT,
            payment_type TEXT,
            status TEXT
            )
    """)
    conn.commit()
    conn.close()

def create_employees_table():
    """Creates the student table if it doesn't exist."""
    conn = sqlite3.connect('z_resters.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT (11) PRIMARY KEY,
            f_name TEXT,
            l_name TEXT,
            email TEXT,
            username TEXT,
            password TEXT,
            wage DECIMAL (8, 2) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def rrr():
    conn = sqlite3.connect('z_resters.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS receiptItems (
            order_id INT (11),
            item_id INT (11),
            quantity INT (3),
            total DECIMAL (8, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES receipts (order_id),
            FOREIGN KEY (item_id) REFERENCES items (item_id)
            )
    """)
    conn.commit()
    
    conn.close()


def employees():
    """Inserts sample data into the student table."""
    conn = sqlite3.connect("z_resters.db")
    cursor = conn.cursor()
    cursor.executemany("""
                       INSERT OR IGNORE INTO employees (emp_id, f_name, l_name, email, username, password, wage) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       [(1, "Ramon", "Parachico", "parachico@gmail.com", "RamonP2", "pass", 20.55),
                        (2, "Lucas", "Chaves", "chaves@gmail.com", "LucasC3", "pass", 20.55),
                        (3, "Sabrina", "Carpenter", "carpenter@gmail.com", "SubwaySandwich", "pass", 20.55)
                        ])
    conn.commit()
    conn.close()

def items():
    connect = sqlite3.connect("z_resters.db")
    cursor = connect.cursor()
    cursor.executemany("""INSERT INTO items (item_id, item_type, item_name, price)
                            VALUES (?, ?, ?, ?)""",
                            [
                                (1, "Beverage", "Coca Cola", 5.0),
                                (2, "Beverage", "Mango Smoothie", 7.25),
                                (3, "Beverage", "Water", 1.25),
                                (4, "Beverage", "Inca Cola", 5.0),
                                (5, "Beverage", "Morocho", 6.25),
                                (6, "Beverage", "Sprite", 5.0),
                                (7, "Beverage", "Strawberry Smoothie", 7.25),
                                (8, "Beverage", "Fanta", 5.0),
                                (9, "Beverage", "Chicha Limena", 5.0),
                                (10, "Beverage", "Iced Tea", 6.25),
                                (11, "Appetizers", "Chips and Guacamole", 2.25),
                                (12, "Appetizers", "Tamales", 5.25),
                                (13, "Appetizers", "Coxinhas", 2.25),
                                (14, "Appetizers", "Humitas", 5.0),
                                (15, "Appetizers", "Pao de Queijo", 2.25),
                                (16, "Appetizers", "Mozzerella Sticks", 3.75),
                                (17, "Appetizers", "Empanadas de Carne", 7.25),
                                (18, "Appetizers", "Empanadas de Queso", 5.25),
                                (19, "Main Course", "Ceviche", 7.25),
                                (20, "Main Course", "Feijoada", 7.25),
                                (21, "Main Course", "Steak Tacos", 8.25),
                                (22, "Main Course", "Pupusas", 5.25),
                                (23, "Main Course", "Salvadoran Tamales", 5.25),
                                (24, "Main Course", "Mofongo", 5.25),
                                (25, "Main Course", "Sopa de Res", 10.25),
                                (26, "Main Course", "Arroz con Habichuelas", 9.99),
                                (27, "Main Course", "Arroz con Tocino", 9.99),
                                (28, "Sides", "Platano Frito", 4.99),
                                (29, "Sides", "Tostones", 4.99),
                                (30, "Sides", "Chicharrones", 6.99),
                                (31, "Sides", "Beans", 2.99),
                                (32, "Sides", "White Rice", 2.99),
                                (33, "Sides", "Mexican Corn Salad", 9.99),
                                (34, "Sides", "Farofa", 4.99),
                                (35, "Sides", "Fries", 2.99),
                                (36, "Desserts", "Tres Leches", 9.99),
                                (37, "Desserts", "Acai Bowl", 9.99),
                                (38, "Desserts", "Brigadeiro", 2.99),
                                (39, "Desserts", "Churros", 1.99),
                                (40, "Desserts", "Flan", 4.99),
                                (41, "Desserts", "Atole de Elote", 7.99),
                                (42, "Desserts", "Quesitos", 4.99),
                                (43, "Desserts", "Arroz con Leche", 4.99),
                                (44, "Desserts", "Arroz con Dulce", 7.99),
                                (45, "Desserts", "Dulce de Leche", 7.99)
                            ]

    )
    connect.commit()
    connect.close()

def orders():
    conn = sqlite3.connect("z_resters.db")
    cursor = conn.cursor()
    cursor.executemany("""
                       INSERT OR IGNORE INTO receipts (order_id, table_number, emp_id, date, time, payment_type, status) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       [(1, 5, 1, "6-20-2024", "5:30 PM", "Credit/Debit", "PAID"),
                        (2, 1, 3, "12-25-2024", "10:00 AM", "Cash", "PAID"),
                        (3, 2, 2, "1-1-2024", "6:30 PM", "Cash", "PAID")
                        ])
    conn.commit()
    conn.close()

def recItems():
    conn = sqlite3.connect("z_resters.db")
    cursor = conn.cursor()
    cursor.executemany("""
                       INSERT OR IGNORE INTO receiptItems (order_id, item_id, quantity, total) 
                       VALUES (?, ?, ?, ?)""", 
                       [(1, 3, 2, 2.50),
                        (1, 36, 1, 9.99),
                        (2, 10, 2, 12.50),
                        (3, 19, 2, 14.50)
                        ])
    conn.commit()
    conn.close()


def tableMaker():
    conn = sqlite3.connect('z_resters.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tables (
            table_number INT (2) PRIMARY KEY,
            available TEXT
            )
    """)
    conn.commit()
    conn.close()

def tablas():
    conn = sqlite3.connect('z_resters.db')
    cursor = conn.cursor()
    cursor.executemany("""INSERT INTO tables (table_number, available)
                       VALUES (?, ?)""",
                       [
                           (1, "AVAILABLE"),
                           (2, "AVAILABLE"),
                           (3, "AVAILABLE"),
                           (4, "AVAILABLE"),
                           (5, "AVAILABLE"),
                           (6, "AVAILABLE"),
                           (7, "AVAILABLE"),
                           (8, "AVAILABLE"),
                           (9, "AVAILABLE"),
                           (10, "AVAILABLE"),
                           (11, "AVAILABLE"),
                           (12, "AVAILABLE"),
                           (13, "AVAILABLE"),
                           (14, "AVAILABLE"),
                           (15, "AVAILABLE"),
                           (16, "AVAILABLE"),
                           (17, "AVAILABLE")
                       ]

    )
    conn.commit()
    conn.close()


create_items_table()
create_receipts_table()
create_employees_table() 
rrr()
tableMaker()

employees()
items()
orders()
recItems()
tablas()


'''
number = 8
with open("orders.txt", "a", newline='') as f:
    f.write(f"{number} ")

number = 9
with open("orders.txt", "a", newline='') as f:
    f.write(f"{number} ")

listofOrders = []
grades_reader=open('orders.txt', 'r')
for row in grades_reader:
    listofOrders = row.split()

print(listofOrders)
'''

'''
# Database Operations
def create_items_table():
    """Creates the student table if it doesn't exist."""
    conn = sqlite3.connect('z_items.db')
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INT (11) PRIMARY KEY,
            item_type TEXT,
            item_name TEXT,
            price DECIMAL (8, 2) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_receipts_table():
    """Creates the student table if it doesn't exist."""
    conn = sqlite3.connect('z_receipts.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            order_id INT (11) PRIMARY KEY,
            table_number INT (2),
            emp_id INT (11),
            date TEXT,
            time TEXT,
            payment_type TEXT,
            status TEXT
            )
    """)
    conn.commit()
    conn.close()

def create_employees_table():
    """Creates the student table if it doesn't exist."""
    conn = sqlite3.connect('z_employees.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT (11) PRIMARY KEY,
            f_name TEXT,
            l_name TEXT,
            email TEXT,
            username TEXT,
            password TEXT,
            wage DECIMAL (8, 2) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def rrr():
    conn = sqlite3.connect('z_receiptItems.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS receiptItems (
            order_id INT (11),
            item_id INT (11),
            quantity INT (3),
            total DECIMAL (8, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES receipts (order_id),
            FOREIGN KEY (item_id) REFERENCES items (item_id)
            )
    """)
    conn.commit()
    
    conn.close()


def employees():
    """Inserts sample data into the student table."""
    conn = sqlite3.connect("z_employees.db")
    cursor = conn.cursor()
    cursor.executemany("""
                       INSERT OR IGNORE INTO employees (emp_id, f_name, l_name, email, username, password, wage) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       [(1, "Ramon", "Parachico", "parachico@gmail.com", "RamonP2", "pass", 20.55),
                        (2, "Lucas", "Chaves", "chaves@gmail.com", "LucasC3", "pass", 20.55),
                        (3, "Sabrina", "Carpenter", "carpenter@gmail.com", "SubwaySandwich", "pass", 20.55)
                        ])
    conn.commit()
    conn.close()

def items():
    connect = sqlite3.connect("z_items.db")
    cursor = connect.cursor()
    cursor.executemany("""INSERT INTO items (item_id, item_type, item_name, price)
                            VALUES (?, ?, ?, ?)""",
                            [
                                (1, "Beverage", "Coca Cola", 5.0),
                                (2, "Beverage", "Mango Smoothie", 7.25),
                                (3, "Beverage", "Water", 1.25),
                                (4, "Beverage", "Inca Cola", 5.0),
                                (5, "Beverage", "Morocho", 6.25),
                                (6, "Beverage", "Sprite", 5.0),
                                (7, "Beverage", "Strawberry Smoothie", 7.25),
                                (8, "Beverage", "Fanta", 5.0),
                                (9, "Beverage", "Chicha Limena", 5.0),
                                (10, "Beverage", "Iced Tea", 6.25),
                                (11, "Appetizers", "Chips and Guacamole", 2.25),
                                (12, "Appetizers", "Tamales", 5.25),
                                (13, "Appetizers", "Coxinhas", 2.25),
                                (14, "Appetizers", "Humitas", 5.0),
                                (15, "Appetizers", "Pao de Queijo", 2.25),
                                (16, "Appetizers", "Mozzerella Sticks", 3.75),
                                (17, "Appetizers", "Empanadas de Carne", 7.25),
                                (18, "Appetizers", "Empanadas de Queso", 5.25),
                                (19, "Main Course", "Ceviche", 7.25),
                                (20, "Main Course", "Feijoada", 7.25),
                                (21, "Main Course", "Steak Tacos", 8.25),
                                (22, "Main Course", "Pupusas", 5.25),
                                (23, "Main Course", "Salvadoran Tamales", 5.25),
                                (24, "Main Course", "Mofongo", 5.25),
                                (25, "Main Course", "Sopa de Res", 10.25),
                                (26, "Main Course", "Arroz con Habichuelas", 9.99),
                                (27, "Main Course", "Arroz con Tocino", 9.99),
                                (28, "Sides", "Platano Frito", 4.99),
                                (29, "Sides", "Tostones", 4.99),
                                (30, "Sides", "Chicharrones", 6.99),
                                (31, "Sides", "Beans", 2.99),
                                (32, "Sides", "White Rice", 2.99),
                                (33, "Sides", "Mexican Corn Salad", 9.99),
                                (34, "Sides", "Farofa", 4.99),
                                (35, "Sides", "Fries", 2.99),
                                (36, "Desserts", "Tres Leches", 9.99),
                                (37, "Desserts", "Acai Bowl", 9.99),
                                (38, "Desserts", "Brigadeiro", 2.99),
                                (39, "Desserts", "Churros", 1.99),
                                (40, "Desserts", "Flan", 4.99),
                                (41, "Desserts", "Atole de Elote", 7.99),
                                (42, "Desserts", "Quesitos", 4.99),
                                (43, "Desserts", "Arroz con Leche", 4.99),
                                (44, "Desserts", "Arroz con Dulce", 7.99),
                                (45, "Desserts", "Dulce de Leche", 7.99)
                            ]

    )
    connect.commit()
    connect.close()

def orders():
    conn = sqlite3.connect("z_receipts.db")
    cursor = conn.cursor()
    cursor.executemany("""
                       INSERT OR IGNORE INTO receipts (order_id, table_number, emp_id, date, time, payment_type, status) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       [(1, 5, 1, "6-20-2024", "5:30 PM", "Credit/Debit", "PAID"),
                        (2, 1, 3, "12-25-2024", "10:00 AM", "Cash", "PAID"),
                        (3, 2, 2, "1-1-2024", "6:30 PM", "Cash", "PAID")
                        ])
    conn.commit()
    conn.close()

def recItems():
    conn = sqlite3.connect("z_receiptItems.db")
    cursor = conn.cursor()
    cursor.executemany("""
                       INSERT OR IGNORE INTO receiptItems (order_id, item_id, quantity, total) 
                       VALUES (?, ?, ?, ?)""", 
                       [(1, 3, 2, 2.50),
                        (1, 36, 1, 9.99),
                        (2, 10, 2, 12.50),
                        (3, 19, 2, 14.50)
                        ])
    conn.commit()
    conn.close()


def tableMaker():
    conn = sqlite3.connect('z_tables.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tables (
            table_number INT (2) PRIMARY KEY,
            available TEXT
            )
    """)
    conn.commit()
    conn.close()

def tablas():
    conn = sqlite3.connect('z_tables.db')
    cursor = conn.cursor()
    cursor.executemany("""INSERT INTO tables (table_number, available)
                       VALUES (?, ?)""",
                       [
                           (1, "AVAILABLE"),
                           (2, "AVAILABLE"),
                           (3, "AVAILABLE"),
                           (4, "AVAILABLE"),
                           (5, "AVAILABLE"),
                           (6, "AVAILABLE"),
                           (7, "AVAILABLE"),
                           (8, "AVAILABLE"),
                           (9, "AVAILABLE"),
                           (10, "AVAILABLE"),
                           (11, "AVAILABLE"),
                           (12, "AVAILABLE"),
                           (13, "AVAILABLE"),
                           (14, "AVAILABLE"),
                           (15, "AVAILABLE"),
                           (16, "AVAILABLE"),
                           (17, "AVAILABLE")
                       ]

    )
    conn.commit()
    conn.close()
'''

'''
def update_table(number):
    #check availability
    check = sqlite3.connect("z_tables.db")
    cursor = check.cursor()
    cursor.execute("SELECT available FROM tables WHERE table_number = ?", (number,))

    item = cursor.fetchone()

    update = sqlite3.connect("z_tables.db")
    uCursor = update.cursor()
    if item[0] == "AVAILABLE":
        uCursor.execute("UPDATE tables SET available = ? WHERE table_number = ?", ("UNAVAILABLE", number,))
    else:
        uCursor.execute("UPDATE tables SET available = ? WHERE table_number = ?", ("AVAILABLE", number,))
    update.commit()
    update.close()


update_table(2)
'''

'''
create_items_table()
create_receipts_table()
create_employees_table() 
rrr()

items()
orders()
recItems()
'''

'''user = input("user? ")
password = input("password? ")

def searcher(user, password):
    conn = sqlite3.connect("z_employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE username = ? AND password = ?", (user, password,))
    
    item = cursor.fetchone()
    
    conn.close()

    if item:
        print(item)
        #print(f" ID: {item[0]}\n First Name: {item[1]}\n Last Name: {item[2]}\n Email: {item[3]}\n Phone Number: {item[4]}\n Username: {item[5]}\n Password: {item[6]}\n Wage: {item[7]}")
    else:
        print("Worker not found.")

searcher(user, password)
'''
print("Database operations completed successfully.")
