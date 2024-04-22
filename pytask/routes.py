from pytask import app, db
from flask import render_template, request, flash, url_for, redirect, jsonify
from sqlalchemy import text

@app.route('/')
def index():
    #todos = Todo.query.join(Project).filter(Project.id == 1, Todo.is_completed == False)()
    #todos = Todo.query.join(Project).filter(Project.id == 1, Todo.is_completed == False).all()
    #unfinished_todos = Todo.query.filter_by(is_completed=False).all()
    #return render_template('app.html', todos=todos, unfinished_todos=unfinished_todos)
    #cookie = request.cookies.get('name') --> Dann auch bei return die variable übergeben
    return render_template('welcome.html')

@app.route('/tasks')
def tasks():
    query = f"select * from t"
    return render_template('tasks.html')

@app.route('/login', methods=['GET', 'POST'])
def login_action():
    print("login was called")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if (username is None or isinstance(username, str) is False or len(username) < 3):
            return render_template('login.html')

        if (password is None or isinstance(password, str) is False or len(password) < 3):
            return render_template('login.html')

        query_stmt = f"select username from user where username = '{username}' and password = '{password}'"
        result = db.session.execute(text(query_stmt))
        user = result.fetchall()
        if not user:
            return render_template('login.html')
        return redirect(url_for('tasks'))
    else:
        print("no post...")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if(username is None or isinstance(username, str) is False or len(username) < 3):
            print("username not valid")
            return render_template('register.html')

        if(email is None or isinstance(email, str) is False or len(email) < 3):
            print("email not valid")
            return render_template('register.html')

        if(password1 is None or
                isinstance(password1, str) is False or
                len(password1) < 3 or
                password1 != password2):
            print("password1 not valid")
            return render_template('register.html')

        query_stmt = f"select * from user where username = '{username}'"
        result = db.session.execute(text(query_stmt))
        item = result.fetchone()

        if item is not None:
            print("Username exists")
            return render_template('register.html')

        query_insert = f"insert into user (username, password, email) values ('{username}', '{password1}', '{email}')"
        db.session.execute(text(query_insert))
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    resp = redirect('/')
    resp.set_cookie('name', '', 0)
    return resp
