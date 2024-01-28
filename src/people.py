import sqlite3 as sql

def load():
  CONNECTION = sql.connect("face-recognition.db")
  cursor = CONNECTION.cursor()
  response = cursor.execute("SELECT * FROM people")
  return response.fetchall()
