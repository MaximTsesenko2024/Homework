import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL    
)''')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', i*10, '1000'))

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = ?', (500, 1))

cursor.execute('DELETE FROM Users WHERE id % 3 = ?', (1,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
result = cursor.fetchall()
for user_data in result:
    print(f'Имя: {user_data[0]} | Почта: {user_data[1]} | Возраст: {user_data[2]} | Баланс: {user_data[3]}')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()[0]
print(f'Количество записей равно: {count}')

cursor.execute('SELECT SUM(balance) FROM Users')
summa = cursor.fetchone()[0]
print(f'Сумма балансов равна: {summa}')

cursor.execute('SELECT AVG(balance) FROM Users')
avg = cursor.fetchone()[0]
print(f'Средний баланс равен: {summa/count}')
connection.commit()
connection.close()
