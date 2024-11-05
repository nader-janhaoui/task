from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello, World!"


# endpoint for add new task
@main.route('/add')
def add():
    return "Add a new task"

# endpoint for delete task
@main.route('/delete')
def delete():
    return "Delete a task"