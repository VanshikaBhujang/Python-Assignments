import sqlite3
from flask_restful import Resource, reqparse

db_location = "students.db"

def connect_to_db():
    conn = sqlite3.connect(db_location)
    return conn

class Students(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=True,
        help="This field cannot be left empty!",
        location='json'
    )
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left empty!",
        location='json'
    )
    parser.add_argument('age',
        type=int,
        required=True,
        location='json'
    )
    parser.add_argument('phone_no',
        type=str,
        location='json'
    )


    def get(self):
        students = []
        try:
            con = connect_to_db()
            con.row_factory = sqlite3.Row
            cursor = con.cursor()

            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            print("hi1")
            for i in rows:
                user = {}
                user["id"] = i["id"]
                user["name"] = i["name"]
                user["age"] = i["age"]
                user["phone_no"] = i["phone_no"]
                students.append(user)
            
            con.commit()
        except:
            students = []
        finally:
            con.close()

        return students

    def post(self):
        if StudentResource.get(id):
            return {'message': "An item with name '{}' already exists".format(id)}, 400
        
        data = Students.parser.parse_args()
        
        s = {
            'id' : data['id'],
            'name': data['name'],
            'age': data['age'],
            'phone_no' : data['phone_no']
        }
        try:
            StudentResource.post(s)
        except:
            return {"message": "Error Occured inserting Item"}, 500
        
        return s, 201

    def put(self):
        data = Students.parser.parse_args()
        student = StudentResource.get(data['id'])

        s = {
            'id': data['id'],
            'name': data['name'],
            'age': data['age'],
            'phone_no': data['phone_no']
        }
        print
        if student=={}:
            try:
                print({'message': "Any record with id '{}' does not exists, so we're inserting the record.".format(data['id'])}, 400)
                StudentResource.post(s)
            except:
                return {"message": "Error occurred Inserting Student"}, 500
        else:
            try:
                StudentResource.put(s)
            except:
                return {"message": "Error occurred Updating Student"}, 500

        return s, 201

    def delete(self):
        data = Students.parser.parse_args()
        connection = connect_to_db()
        cursor = connection.cursor()

        if StudentResource.get(data['id'])=={}:
            return {'message': "An item with id '{}' does'nt exists".format(data['id'])}, 400

        query = "DELETE FROM users WHERE id=?"
        cursor.execute(query, (data['id'],))
        connection.commit()
        connection.close()

        return {'message': 'Student Deleted'}, 201


class StudentResource(Resource):

    def get(id):
        user = {}
        try:
            conn = connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            print(id)
            cur.execute("SELECT * FROM users WHERE id = ?", 
                        (id,))
            row = cur.fetchone()
            user["id"] = row["id"]
            user["name"] = row["name"]
            user["age"] = row["age"]
            user["phone_no"] = row["phone_no"]
        except:
                user = {}
        return user
    
    
    def post(student):
        inserted_user = {}

        try:
            con = sqlite3.connect('students.db')
            cur=con.cursor()
            query = "INSERT INTO users VALUES(?, ?, ?, ?)"
            cur.execute(query, (student['id'], student['name'], student['age'], student['phone_no']))
            con.commit()
            inserted_user = StudentResource.get(cur.lastrowid)
        except:
            con.rollback()
        finally:
            con.close()

        return inserted_user

    def put(student):
        con = connect_to_db()
        cursor = con.cursor()
        
        query = "UPDATE users SET name=?, age=?, phone_no=? WHERE id=?"
        cursor.execute(query, (student['name'], student['age'], student['phone_no'], student['id']))
        con.commit()
        con.close()