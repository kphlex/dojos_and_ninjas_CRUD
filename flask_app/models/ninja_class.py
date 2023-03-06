from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo_class
from flask import flash

class Ninja:
    DB = "dn_db"
    def __init__(self, data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_name = None
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninjas in results:
            ninjas.append(cls(ninjas))
        return ninjas
    
    # CRUD METHODS
    
    #CREATE
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO ninjas 
                ( dojo_id, first_name , last_name , age , created_at, updated_at ) 
                VALUES 
                ( %(dojo_id)s, %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() )
                ;"""
        return connectToMySQL(cls.DB).query_db( query, data )
    
    #READ 
    @classmethod
    def get_all(cls):
        query = """SELECT * 
                FROM ninjas
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas
    
    #READ ALL NINJAS WITH DOJO NAME - /ninjas table
    @classmethod
    def get_ninjas_with_dojo_name(cls):
        query = """SELECT * 
                FROM ninjas
                LEFT JOIN dojos
                ON ninjas.dojo_id = dojos.id
                ;"""
        results = connectToMySQL(cls.DB).query_db( query)
        ninjas = []
        for row in results:
            ninja = cls(row)
            dojo_data = {
                'id': row["dojos.id"],
                'name': row["name"],
                'created_at' : row["dojos.created_at"],
                'updated_at' : row["dojos.updated_at"],
            }
            ninja.dojo_name = dojo_class.Dojo(dojo_data)
            ninjas.append(ninja)
        return ninjas
        
    #READ ONE NINJA
    @classmethod 
    def get_one(cls, data):
        query = """SELECT * 
                FROM ninjas 
                WHERE id = %(id)s
                ;"""
        results = connectToMySQL(cls.DB).query_db( query, data)
        return cls(results[0])
    #UPDATE
    @classmethod
    def update(cls, data):
        query = """
                UPDATE ninjas 
                SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() 
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        
        return results
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM ninjas
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    # @classmethod
    # def delete_ninjas_then_dojo(cls, data):
    #     query = """
    #             DELETE * 
    #             FROM ninjas
    #             LEFT JOIN dojos
    #             ON ninjas.dojo_id = dojos.id
    #             WHERE dojos.id = %(id)s
    #             ;"""
    #     query_two = """
    #                 DELETE FROM dojos
    #                 WHERE dojos.id = %(id)s
    #                 ;"""
    #     results = connectToMySQL(cls.DB).query_db(query, data)
    #     two_results = connectToMySQL(cls.DB).query_db(query_two, data)
    #     return results, two_results
    
    #VALIDATION
    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        if len(ninja['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['last_name'])  < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['age']) < 2:
            flash("Age must be at least 2 characters.")
        return is_valid