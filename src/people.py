import sqlite3 as sql

def load():
  """
  Load all the records from the 'people' table in the 'face-recognition.db' database.

  Returns:
    A list of tuples representing the records from the 'people' table.
  """
  CONNECTION = sql.connect("face-recognition.db")
  
  cursor = CONNECTION.cursor()
  response = cursor.execute("SELECT * FROM people")
  list = response.fetchall()
  
  CONNECTION.close()
  return list

