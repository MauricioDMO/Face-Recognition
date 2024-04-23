import sqlite3 as sql


def init():
    CONNECTION = sql.connect("face-recognition.db")
    cursor = CONNECTION.cursor()

    # ? Create the table roles.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS roles (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  name text,
                  description text
                )"""
    )

    # ? Create the table buildings.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS buildings (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  building text NOT NULL
                )"""
    )

    # ? Create the table classrooms.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS classrooms (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  classroom text NOT NULL,
                  building_id integer NOT NULL,
                  FOREIGN KEY (building_id)
                    REFERENCES buildings (id)
                )"""
    )

    # ? Create the table days.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS days (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  day text NOT NULL
                )"""
    )

    # ? Create the table hours.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS hours (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  start_time text NOT NULL,
                  end_time text NOT NULL
                )"""
    )

    # ?  Create the table schedules.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS schedules (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  day_id integer NOT NULL,
                  hour_id integer NOT NULL,
                  FOREIGN KEY (day_id)
                    REFERENCES days (id)
                  FOREIGN KEY (hour_id)
                    REFERENCES hours (id)
                )"""
    )

    # ? Create the table subjects.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS subjects (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  name text NOT NULL
                )"""
    )

    # ? Create the table states.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS states (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  state text NOT NULL
                )"""
    )

    # ? Create the table classes.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS classes (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  classroom_id integer NOT NULL,
                  schedule_id integer NOT NULL,
                  subject_id integer NOT NULL,
                  state_id integer NOT NULL,
                  FOREIGN KEY (state_id)
                    REFERENCES states (id)
                  FOREIGN KEY (schedule_id)
                    REFERENCES schedules (id)
                  FOREIGN KEY (subject_id)
                    REFERENCES subjects (id)
                  FOREIGN KEY (classroom_id)
                    REFERENCES classrooms (id)
                )"""
    )

    # ? Create the table people.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS people (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  name text NOT NULL,
                  lastname text NOT NULL,
                  carnet text,
                  role_id integer NOT NULL,
                  state_id integer NOT NULL,
                  FOREIGN KEY (role_id)
                    REFERENCES roles (id)
                  FOREIGN KEY (role_id)
                    REFERENCES roles (id)
                )"""
    )

    # ? Create the table images.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS images (
                id integer PRIMARY KEY AUTOINCREMENT,
                people_id integer NOT NULL,
                image blob NOT NULL,
                FOREIGN KEY (people_id)
                  REFERENCES people (id)
              )"""
    )

    # ? Create the table classes_people.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS classes_people (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  person_id integer NOT NULL,
                  class_id integer NOT NULL,
                  FOREIGN KEY (person_id)
                    REFERENCES people (id)
                  FOREIGN KEY (class_id)
                    REFERENCES classes (id)
                )"""
    )

    # ? Create the table assists.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS assists (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  date text NOT NULL,
                  time text NOT NULL,
                  person_id integer NOT NULL,
                  class_id integer NOT NULL,
                  FOREIGN KEY (person_id)
                    REFERENCES people (id)
                  FOREIGN KEY (class_id)
                    REFERENCES classes (id)
                )"""
    )

    CONNECTION.close()
