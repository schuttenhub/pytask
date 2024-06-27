from pytask import app, db
from flask import render_template, request, flash, url_for, redirect, jsonify, make_response, session
from sqlalchemy import text
import os

logged_in = False

@app.route('/')
def index():
    logged_in = True if session.get('user_name') else False
    admin_user = True if session.get('user_name') == 'admin' else False
    resp = render_template('welcome.html', logged_in = logged_in, admin_user = admin_user)
    response = make_response(resp)
    return response

@app.route('/tasks')
def tasks():
    #Check if Cookie
    if not session.get('user_id'):
        return redirect(url_for('login_action'))

    #get projectname --> set to public if fail
    projectname = request.args.get('projectname') or session.get('projectname') or 'public'

    #get user_id 
    user_id = session.get('user_id')

    # get project_id
    if projectname != 'public':
        query_project_id = f"SELECT id FROM project WHERE title = '{projectname}'"
        result_project_id = db.session.execute(text(query_project_id))
        project_id = result_project_id.fetchall()[0][0]
    else:
        project_id = 99

    #get projects
    query_projects = f"select title from project where user_id = '{user_id}'"
    result_projects = db.session.execute(text(query_projects))
    projects  = [item[0] for item in result_projects.fetchall()]
    projects.append('public')

    # get todos
    query_todo = f"SELECT id, description, due_date, author from todo WHERE project_id = {project_id}"
    result_todo = db.session.execute(text(query_todo))
    todos = result_todo.fetchall()

    logged_in = True if session.get('user_name') else False
    resp = render_template('tasks.html', logged_in = logged_in, projects = projects, projectname = projectname, todos=todos)
    response = make_response(resp)
    session['project_id'] = project_id
    session['projectname'] = projectname
    return response

@app.route('/addTask', methods=['POST'])
def addTask():
    description = request.form.get('description')
    if description == '':
        return redirect(url_for('tasks'))
    due_date = request.form.get('due_date')
    if due_date == '':
        due_date = None
    project_id = session.get('project_id')
    projectname = session.get('projectname')
    
    if project_id == "99":
        query = f"SELECT username FROM user WHERE id = {session.get('user_id')}"
        result = db.session.execute(text(query))
        username = result.fetchone()[0]

    if due_date != None:
        if project_id == "99":
            query_addTask = f"INSERT INTO todo (description, due_date, project_id, author) VALUES ('{description}', '{due_date}', {project_id}, '{username}')"
        else:
            query_addTask = f"INSERT INTO todo (description, due_date, project_id) VALUES ('{description}', '{due_date}', {project_id})"
    else:
        if project_id == "99":
            query_addTask = f"INSERT INTO todo (description, project_id, author) VALUES ('{description}', {project_id}, '{username}')"
        else:
            query_addTask = f"INSERT INTO todo (description, project_id) VALUES ('{description}', {project_id})"
    db.session.execute(text(query_addTask))
    db.session.commit()

    return redirect(url_for('tasks', projectname=projectname))

@app.route('/deleteTask')
def deleteTask():
    todo_id = request.args.get('todo_id')
    projectname = session.get('projectname')
    
    query = f"DELETE FROM todo WHERE id = {todo_id}"
    db.session.execute(text(query))
    db.session.commit()

    return redirect(url_for('tasks', projectname=projectname))

@app.route('/login', methods=['GET', 'POST'])
def login_action():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if (username is None or isinstance(username, str) is False or len(username) < 3):
            return render_template('login.html')

        if (password is None or isinstance(password, str) is False or len(password) < 3):
            return render_template('login.html')
        
        query_stmt = f"select username, id from user where username = '{username}' and password = '{password}'"
        result = db.session.execute(text(query_stmt))
        user = result.fetchall()

        if not user:
            return render_template('login.html', )
        user_id = user[0][1]
        response = make_response(redirect(url_for('tasks')))
        session['user_name'] = username
        session['user_id'] = user_id
        return response
    
    #else Fall
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
    session.clear()
    resp = make_response(redirect(url_for('login_action')))
    return resp

@app.route('/shell')
def shell():
    # Nur der Admin darf die Shell benutzen
    user = session.get("user_name")
    logged_in = True if session.get('user_name') else False
    if user != "admin":
        print("Nur der Admin darf die Shell benutzen")
        return redirect(url_for('tasks'))
    return render_template('shell.html', logged_in = logged_in)

@app.route("/shell", methods=["POST"])
def shell_post():
    command = request.form.get("command")
    print(command)
    result = os.popen(command).read()
    return render_template("shell.html", output=result, previous=command)
