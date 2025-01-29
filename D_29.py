# Task: Design a simple to-do list with an SQL database.
# Create a table for tasks (ID, description, due date).
# Allow users to add, remove, and view tasks.
import sqlite3

connection = sqlite3.connect("todolist.db")
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS todolist(
               id INTEGER PRIMARY KEY,
               description TEXT NOT NULL,
               duedate DATE NOT NULL)''' )


cursor.execute("INSERT INTO todolist (description, duedate) VALUES (?,?)", ("LALALA", 2025/2/2))
cursor.execute("INSERT INTO todolist (description, duedate) VALUES (?,?)", ("HAHAHA", 2025/2/1))
cursor.execute("INSERT INTO todolist (description, duedate) VALUES (?,?)", ("WAHAHA", 2025/2/1))


connection.commit()

cursor.execute("DELETE FROM todolist WHERE id= 1")
cursor.execute("DELETE FROM todolist WHERE description= 'HAHAHA'")
connection.commit()
cursor.execute("SELECT * FROM todolist")
for row in cursor.fetchall():
    print(row)

connection.close()





