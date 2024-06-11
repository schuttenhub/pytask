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


