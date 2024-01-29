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
  