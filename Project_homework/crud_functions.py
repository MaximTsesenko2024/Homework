import sqlite3


def conect(filename: str):
    conection = sqlite3.connect(filename)
    conection = initiate_db(conection)
    return conection


def initiate_db(conection: sqlite3.Connection):
    cursor = conection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    filename TEXT)
    ''')
    cursor.execute('''
     CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)   
    ''')
    conection.commit()
    return conection


def is_included(username: str, conection: sqlite3.Connection):
    cursor = conection.cursor()
    user = cursor.execute('''SELECT id FROM Users WHERE username = ?''', (username,)).fetchone()
    return user is not None


def add_user(username: str, email: str, age: int, conection: sqlite3.Connection):
    if is_included(username, conection):
        return conection
    else:
        cursor = conection.cursor()
        cursor.execute('''INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)''',
                       (username, email, age, 1000))
        conection.commit()
    return conection


def get_all_products(cursor: sqlite3.Cursor):
    cursor.execute("""
    SELECT title, description, price, filename FROM Products
    """)
    products = cursor.fetchall()
    return products


def exit_db(conection: sqlite3.Connection):
    conection.close()

if __name__ == '__main__':
    product_list = [
        {'filename': 'Image/C.jpg', 'name': 'Витамин С', 'text': 'Витамин С'},
        {'filename': 'Image/D3.jpg', 'name': 'Витамин D3', 'text': 'Витамин D3'},
        {'filename': 'Image/B_g.jpg', 'name': 'Витамины B', 'text': 'Витамины группы B'},
        {'filename': 'Image/Se+Zn.jpg', 'name': 'Se+Zn', 'text': 'Витамины с добавлением силена и цинка'},
    ]
    conection = conect('database.db')
    conection = initiate_db(conection)
    cursor = conection.cursor()
    for i in range(len(product_list)):
        cursor.execute('INSERT INTO Products (title, description, price, filename) VALUES (?, ?, ?, ?)',
                       (product_list[i]['name'], product_list[i]['text'], (i+1)*100, product_list[i]['filename']))
        conection.commit()

    products = get_all_products(cursor)
    for i in products:
        print(i)
    exit_db(conection)

