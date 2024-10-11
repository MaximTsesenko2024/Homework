import sqlite3


def conect(filename: str):
    conection = sqlite3.connect(filename)
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

