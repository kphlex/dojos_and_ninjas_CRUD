from flask_app import app
from flask import render_template, redirect, request, session, flash



#HOME ROUTE
@app.route('/')
def index():
    return render_template('home.html')

#CREATE ROUTE
@app.route('/create')
def create_page():
    return render_template('create.html')

#VIEW ROUTE
@app.route('/view')
def view_page():
    return render_template('view.html')

#ABOUT ROUTE
@app.route('/about')
def about():
    return render_template('about.html')


#CREATE DOJO FORM PAGE 
@app.route('/create_dojo_page')
def create_dojo_form():
    return render_template('create_dojo.html')

