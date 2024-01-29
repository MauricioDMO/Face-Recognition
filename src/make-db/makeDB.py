import sqlite3 as sql

conn = sql.connect("face-recognition.db")
cursor = conn.cursor()


#? Create the table roles.
cursor.execute("""CREATE TABLE IF NOT EXISTS roles (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text,
                description text
              )""")


#? Create the table people.
cursor.execute("""CREATE TABLE IF NOT EXISTS people (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                lastname text NOT NULL,
                carnet text,
                image blob NOT NULL,
                role_id int NOT NULL,
                FOREIGN KEY (role_id)
                  REFERENCES roles (id)
              )""")


#? Create the table buildings.
cursor.execute("""CREATE TABLE IF NOT EXISTS buildings (
                id integer PRIMARY KEY AUTOINCREMENT,
                building text NOT NULL,
              )""")


#? Create the table classrooms.
cursor.execute("""CREATE TABLE IF NOT EXISTS classrooms (
                id integer PRIMARY KEY AUTOINCREMENT,
                classroom text NOT NULL,
                building_id int NOT NULL,
                FOREIGN KEY (building_id)
                  REFERENCES buildings (id)
              )""")


#? Create the table assists.
cursor.execute("""CREATE TABLE IF NOT EXISTS assists (
                id integer PRIMARY KEY AUTOINCREMENT,
                date text NOT NULL,
                time text NOT NULL,
                person_id int NOT NULL,
                building_id int NOT NULL,
                FOREIGN KEY (person_id)
                  REFERENCES people (id)
                FOREIGN KEY (building_id)
                  REFERENCES buildings (id)
              )""")

conn.close()