import sqlite3

db_location = "students.db"

def create_Table():
    con = sqlite3.connect(db_location)
    cursor = con.cursor()
    try:
        con.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                age INT,
                phone_no TEXT
            );
        ''')

        con.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        con.close()

def delete_Table():
    con = sqlite3.connect(db_location)
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS students")
    
    con.commit()
    con.close()