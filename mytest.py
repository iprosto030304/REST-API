import sqlite3

connection = sqlite3.connect('data1.db')

cursor = connection.cursor()

select_query = "SELECT * FROM users"
cursor.execute(select_query)
print(cursor.execute)