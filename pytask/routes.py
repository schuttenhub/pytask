from pytask import app, db
from flask import render_template, request, flash, url_for, redirect, jsonify, make_response
from sqlalchemy import text

logged_in = False

def return_site(site_name):
    logged_in = True if request.cookies.get('user_name') else False
    resp = render_template(f'{site_name}', logged_in = logged_in)
    response = make_response(resp)
    return response

@app.route('/')
def index():
    return return_site('welcome.html')

@app.route('/tasks')
def tasks():

    #Check if cookie
    if not request.cookies.get('user_id'):
        return redirect(url_for('login_action'))

    #get projectname --> set to public if fail
    projectname = request.args.get('projectname') or request.cookies.get('projectname') or 'public'

    #get user_id 
    user_id = request.cookies.get('user_id')

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


    logged_in = True if request.cookies.get('user_name') else False
    resp = render_template('tasks.html', logged_in = logged_in, projects = projects, projectname = projectname, todos=todos)
    response = make_response(resp)
    response.set_cookie('project_id', f'{project_id}')
    response.set_cookie('projectname', f'{projectname}')
    return response

@app.route('/addTask', methods=['POST'])
def addTask():
    description = request.form.get('description')
    if description == '':
        return redirect(url_for('tasks'))
    due_date = request.form.get('due_date')
    if due_date == '':
        due_date = None
    project_id = request.cookies.get('project_id')
    projectname = request.cookies.get('projectname')
    
    if project_id == "99":
        query = f"SELECT username FROM user WHERE id = {request.cookies.get('user_id')}"
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
    projectname = request.cookies.get('projectname')
    
    query = f"DELETE FROM todo WHERE id = {todo_id}"
    db.session.execute(text(query))
    db.session.commit()

    return redirect(url_for('tasks', projectname=projectname))

#@app.route('/createProject')
#def createProject():
    

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
        response.set_cookie('user_name', f'{username}')
        response.set_cookie('user_id', f'{user_id}')
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
    resp = make_response(redirect(url_for('login_action')))
    resp.set_cookie('user_name', '', expires=0)
    resp.set_cookie('user_id', '', expires=0)
    return resp


# Injections:
## Login:
    # Beim username folgendes eingeben: ' OR id = 1; -- 
    # Passwort mit mehr als 3 Zeichen befüllen und go :)
    # Anmeldung erfolgt mit dem user, welcher die eingetragene ID hat

## deleteTask:
    # Sagen wir ich habe diesen Link: http://127.0.0.1:8099/deleteTask?todo_id=25
    # Ich könnte das draus machen: http://127.0.0.1:8099/deleteTask?todo_id=1 OR description IS NOT NULL; -- 
    
    
# Zum Todos wiederherstellen:
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (1, 'Build a Flask app', '2024-05-01 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (2, 'Finalize project scope', '2024-04-15 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (4, 'Implement authentication system', '2024-04-25 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (5, 'Develop the user profile section', '2024-05-05 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (6, 'Setup database backups', '2024-05-10 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (7, 'Run user acceptance testing', '2024-05-15 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (8, 'Deploy the application to production', '2024-05-20 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (9, 'Conduct post-launch review meeting', '2024-05-25 00:00:00', 4, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (10, 'Salat', NULL, 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (16, 'asdasd', '2024-04-27 19:00:00', 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (18, 'test', NULL, 2, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (23, 'alio', NULL, 4, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (24, 'hehe', NULL, 99, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (25, 'hehe2', NULL, 99, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (26, 'testserfsdf', NULL, 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (27, 'sdfsdf', '2024-04-30 15:14:00', 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (28, 'asdasd', NULL, 4, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (29, 'asdasd', NULL, 2, 0);
