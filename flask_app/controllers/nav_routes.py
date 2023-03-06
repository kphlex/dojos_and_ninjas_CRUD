from flask_app import app
from flask import render_template, redirect, request, session, flash


#REGISTRATION / LOGIN
@app.route('/')
def start():
    if 'email' in session:
        return redirect ('/dashbaord')
    return redirect('/login')

#HOME ROUTE
@app.route('/dashboard')
def index():
    if "email" in session:
        return render_template('home.html')
    return redirect('/login')

#CREATE ROUTE
@app.route('/create')
def create_page():
    if "email" not in session:
        return redirect('/login')
    return render_template('create.html')

#VIEW ROUTE
@app.route('/view')
def view_page():
    if "email" not in session:
        return redirect('/login')
    return render_template('view.html')

#ABOUT ROUTE
@app.route('/about')
def about():
    return render_template('about.html')


#CREATE DOJO FORM PAGE 
@app.route('/create_dojo_page')
def create_dojo_form():
    return render_template('create_dojo.html')

