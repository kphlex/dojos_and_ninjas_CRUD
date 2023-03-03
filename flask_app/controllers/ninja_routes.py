from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja_class import Ninja
from flask_app.models.dojo_class import Dojo



#READ ALL NINJAS
@app.route('/ninjas')
def read():
    return render_template('table_ninjas.html', ninjas = Ninja.get_all(), dojo_id = Dojo.get_dojos_with_ninjas())

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/ninjas')

@app.route('/ninja/show/<int:id>')
def show_one(id):
    data = {
        'id': id
    }
    return render_template('ninja.html', ninja = Ninja.get_one(data))

@app.route('/ninja/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

@app.route('/ninja/update', methods = ['POST'])
def update():
    updated_id = request.form['id']
    Ninja.update(request.form)
    return redirect(f'/ninja/show/{updated_id}')


@app.route('/ninja/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Ninja.delete(data)
    return redirect('/ninjas')


@app.route('/create_ninja_page')
def create_ninja_form():
    
    return render_template('create_ninja.html', dojo_list = Dojo.get_all_dojos())

