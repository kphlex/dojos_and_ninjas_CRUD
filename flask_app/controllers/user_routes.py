from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_class import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)




#REGISTRATION FORM 
@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        return redirect('/register')
    else:
        session.clear()
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
    }
    
    user_id = User.save_user(data)
    session['user_id'] = user_id
    return redirect('/login')

#REGISTRATION FORM PAGE
@app.route('/register')
def register_user():
    return render_template('register.html')


#LOGIN FORM
@app.route('/login/user', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    
    if not user_in_db:
        flash('Invalid Email/Password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/home')
    session['email'] = user_in_db.email
    return redirect('/dashboard')


#LOGIN FORM PAGE
@app.route('/login')
def login_user():
    return render_template('login.html')

#LOGOUT
@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/login')