import os
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

TODO = [
    {
        "id": uuid.uuid4().hex,
        "todo": "test_Todo",
        "assignee": "Test_assignee",
        "done": False
    }

]


@app.route('/todos', methods=['GET', 'POST'])
def all_todos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TODO.append({
            'id': uuid.uuid4().hex,
            'todo': post_data.get('todo'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Todo added!'
    else:
        response_object['todo'] = TODO
    return jsonify(response_object)


@app.route('/todos/<todo_id>', methods=['GET', 'PUT', 'DELETE'])
def single_todo(todo_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        # TODO: refactor to a lambda and filter
        return_todo = ''
        for todo in TODO:
            if todo['id'] == todo_id:
                return_todo = todo
        response_object['todo'] = return_todo
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_todo(todo_id)
        TODO.append({
            'id': uuid.uuid4().hex,
            'todo': post_data.get('todo'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Todo updated!'
    if request.method == 'DELETE':
        remove_todo(todo_id)
        response_object['message'] = 'Todo removed!'
    return jsonify(response_object)


def remove_todo(todo_id):
    for todo in TODO:
        if todo['id'] == todo_id:
            TODO.remove(todo)
            return True
    return False



if __name__ == '__main__':
    app.run(debug=True, port=8080)
