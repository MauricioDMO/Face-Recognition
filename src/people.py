import sqlite3 as sql

def loadAllPeople():
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


def addPerson(name: str, lastname: str, carnet: str, image: str, role_id: str):
  """
  Add a person to the database.
  Submit data with object destructuring.

  Args:
    name (str): The person's first name.
    lastname (str): The person's last name.
    carnet (str): The person's identification number (optional).
    image (str): The path to the person's image.
    role_id (int): The person's id role.

  Returns:
    None
  """
  
  with open(image, "rb") as img:
    image = img.read()
  
  CONNECTION = sql.connect("face-recognition.db")
  
  cursor = CONNECTION.cursor()
  
  cursor.execute("""INSERT INTO people
                 (name, lastname, carnet, image, role_id, state_id)
                 VALUES
                 (?, ?, ?, ?, ?, 1)""", (name, lastname, carnet, image, role_id))
  CONNECTION.commit()
  CONNECTION.close()
  