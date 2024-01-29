import sqlite3 as sql

def init():
  CONNECTION = sql.connect("face-recognition.db")
  cursor = CONNECTION.cursor()
  
  #? insert roles into the table roles.
  cursor.execute("""INSERT INTO roles (name, description)
                  VALUES ("Administacion", "Personal de administracion"),
                         ("Seguridad", "Personal de seguridad"),
                         ("Profesor", "Profesor"),
                         ("Estudiante", "Estudiante")
                         """)
  CONNECTION.commit()
  
  #? insert buildings into the table buildings.
  cursor.execute("""INSERT INTO buildings (building)
                  VALUES ("A"),
                         ("B"),
                         ("C"),
                         ("D"),
                         ("E"),
                         ("EBLE"),
                         ("Posgrado")
                        """)
  CONNECTION.commit()
  
  classrooms = [
    ("21-22", 1),
    ("23-24", 1),
    ("25-26", 1),
    ("27-28", 1),
    ("31-32", 1),
    ("33-34", 1),
    ("35-36", 1),
    ("37-38", 1),
    ("41-42", 1),
    ("43-44", 1),
    ("45-46", 1),
    ("47-48", 1)
  ]
  
  #? insert classrooms into the table classrooms.
  cursor.execute("""INSERT INTO classrooms (classroom, building_id) values (?, ?)""", classrooms)
  CONNECTION.commit()