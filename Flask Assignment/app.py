from flask import Flask, jsonify, request
from flask_restful import Api
from test import create_Table
from student import Students, StudentResource


app=Flask(__name__)
api= Api(app)

@app.before_first_request
def create_table():
    create_Table()

api.add_resource(Students, '/student')
api.add_resource(StudentResource, '/studentResource/<int:id>')
# api.add_resource(StudentResource, '/studentResource<student>')


if __name__ == "__main__":
    app.run(debug=True)
