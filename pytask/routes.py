from pytask import app, User, Project, Todo, db
from flask import render_template
from flask import request, jsonify

@app.route('/')
def index():
    #todos = Todo.query.join(Project).filter(Project.id == 1, Todo.is_completed == False)()
    todos = Todo.query.join(Project).filter(Project.id == 1, Todo.is_completed == False).all()
    unfinished_todos = Todo.query.filter_by(is_completed=False).all()
    return render_template('app.html', todos=todos, unfinished_todos=unfinished_todos)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



# Todo Applications
@app.route('/todo/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    # Assuming you have a Todo model and it's already imported
    todo = Todo.query.get(todo_id)
    if todo:
        todo.is_completed = True  # Set is_completed to True directly
        db.session.commit()
        return jsonify({'success': True, 'message': 'Todo marked as completed.'})
    else:
        return jsonify({'success': False, 'message': 'Todo not found.'}), 404

@app.route('/uncomplete_all', methods=['POST'])
def uncomplete_all_todos():
    try:
        Todo.query.update({Todo.is_completed: False})
        db.session.commit()
        return jsonify({'success': True, 'message': 'All todos marked as incomplete.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
