import sqlite3 as sql

conn = sql.connect("face-recognition.db")
cursor = conn.cursor()


#? Create the table roles.
cursor.execute("""CREATE TABLE IF NOT EXISTS roles (
                id integer PRIMARY KEY,
                name text,
                description text
              )""")


#? Create the table people.
cursor.execute("""CREATE TABLE IF NOT EXISTS people (
                id integer PRIMARY KEY,
                name text NOT NULL,
                lastname text NOT NULL,
                carnet text NOT NULL,
                image blob NOT NULL,
                role_id int NOT NULL,
                FOREIGN KEY (role_id)
                  REFERENCES roles (id)
              )""")


#? Create the table buildings.
cursor.execute("""CREATE TABLE IF NOT EXISTS buildings (
                id integer PRIMARY KEY,
                building text NOT NULL,
                classroom text NOT NULL
              )""")


#? Create the table assists.
cursor.execute("""CREATE TABLE IF NOT EXISTS assists (
                id integer PRIMARY KEY,
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