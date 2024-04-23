from pytask import app, db
from flask import render_template, request, flash, url_for, redirect, jsonify, make_response
from sqlalchemy import text

logged_in = False

def return_site(site_name):
    logged_in = True if request.cookies.get('user_name') else False
    resp = render_template(f'{site_name}', logged_in = logged_in)
    response = make_response(resp)
    print("Login Status =", logged_in)
    return response

@app.route('/')
def index():
    return return_site('welcome.html')

@app.route('/tasks')
def tasks():
    #get user_id 
    user_id = request.cookies.get('user_id')
    #get projects
    query_projects = f"select * from project where id = '{user_id}'"
    result_projects = db.session.execute(text(query_projects))
    projects = result_projects.fetchall()

    # Jetzt Projekte in die sidebar packen

    # Dann Button machen, der neue Projekte in der Sidebar erstellen kann


    logged_in = True if request.cookies.get('user_name') else False
    resp = render_template(f'{site_name}', logged_in = logged_in)
    response = make_response(resp)
    print("Login Status =", logged_in)
    return response

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
    resp = redirect('/')
    resp.set_cookie('user_name', '', 0)
    resp.set_cookie('user_id', '', 0)
    return resp
