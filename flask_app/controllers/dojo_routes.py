from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_class import Dojo





#CREATE DOJO FORM 
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save_dojo(request.form)
    
    return redirect('/dojos')

#READ DOJO TABLE
@app.route('/dojos')
def read_dojos():
    
    return render_template('table_dojos.html', dojos = Dojo.get_all_dojos())


#READ DOJO BY ID WITH NINJAS ASSOCIATED
@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {
        "id": id,
    }
    return render_template('dojo.html', dojo = Dojo.get_dojo_with_ninjas(data))




#DELETE
@app.route('/dojo/delete/<int:id>')
def delete_dojo(id):
    data = {
        'id': id
    }
    Dojo.delete_dojo(data)
    return redirect('/dojos')