import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor() 

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
age INTEGER
) ''')
connection.commit()

def Add():
    print ('Enter the username')
    username = input()
    print ('Enter the age')
    age = int(input())
    cursor.execute('INSERT INTO Users (username, age) VALUES (?, ?)', (username, age))
    connection.commit()
    connection.close()
def Delete():
    print('''
    Chose the action:
    [1] Delete by num
    [2] Delete all
    ''')
    action = input()
    def DeleteByNum():
        print('Type the num of user')
        user = input()
        cursor.execute('DELETE FROM Users WHERE id = ?', (user,))
    def DeleteAll():
        cursor.execute('TRUNCATE TABLE Users')
    if action == '1':
        DeleteByNum()
    elif action == '2':
        DeleteAll()
    else:
        print('Unknown operation')
def View():
    print('''
    Chose the action:
    [1] View by num
    [2] View all
    ''')
    action = input()
    def ViewAll():
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()
        for user in users:
            print(user)
    def ViewByNum():
        print('Type the num of user')
        num = input()
        cursor.execute('SELECT * FROM Users WHERE id = ?', (num,))
        user = cursor.fetchone()
        print(user)
    if action == '1':
        ViewByNum()
    elif action == '2':
        ViewAll()
    else:
        print('Unknown operation')
