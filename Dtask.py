import sqlite3

connection = sqlite3.connect("book.db")
cursor = connection.cursor()

#create a table for products
cursor.execute('''CREATE TABLE IF NOT EXISTS BOOKS (
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               author TEXT NOT NULL,
               price REAL NOT NULL
               )''')
#insert data
cursor.execute("INSERT INTO BOOKS (title, author, price) VALUES (?, ?,?)", ("science", "Ram" ,999.99))
cursor.execute("INSERT INTO BOOKS (title, author, price) VALUES (?, ?,?)", ("math", "hari" ,99))
cursor.execute("INSERT INTO BOOKS(title, author, price) VALUES (?, ?,?)", ("nepali", "shyam" ,109))

connection.commit()

#fetch data
cursor.execute("SELECT * FROM BOOKS")
for row in cursor.fetchall():
    print(row)

UPDATE BOOKS  
SET author = "yang" WHERE title = science;


connection.close()

