from random import randint

from flask import Flask, escape, request, jsonify

app = Flask(__name__)

students = {}
classes = {}

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {escape(name)}!'

@app.route('/<string:name>')
def hello(name):
    return f'Hello, {escape(name)}!'

@app.route('/students/', methods=['POST'])
def post_student():
    student_id = randint(10000, 20000)
    content = request.json
    student = {"id": student_id, "name": content["name"]}
    students[student_id] = student
    return students[student_id], 201

@app.route('/students/<int:id>')
def get_student(id):
    return students[id], 201

@app.route('/classes/', methods=['POST'])
def post_class():
    class_id = randint(100, 300)
    content = request.json
    class_info = {"id": class_id, "name": content["name"], "students": list()}
    classes[class_id] = class_info
    return classes[class_id], 201

@app.route('/classes/<int:id>')
def get_class(id):
    return classes[id], 201

@app.route('/classes/<int:id>', methods=['PATCH'])
def add_student_to_class(id):
    content = request.json
    student_id = content["id"]
    classes[id]["students"].append(students[student_id])
    return classes[id], 201
