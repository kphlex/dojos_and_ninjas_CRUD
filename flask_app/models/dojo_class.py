from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_class

class Dojo:
    DB = "dn_db"
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def save_dojo( cls , data ):
        query = """INSERT INTO dojos (name, created_at, updated_at) 
                VALUES (%(name)s, NOW(), NOW())
                ;"""
        result = connectToMySQL(cls.DB).query_db( query, data)
        print(result)
        return result
    
    
    #READ 
    @classmethod
    def get_all_dojos(cls):
        query = """SELECT * 
                FROM dojos
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    
    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = """SELECT * FROM dojos 
                LEFT JOIN ninjas  
                ON ninjas.dojo_id = dojos.id 
                WHERE dojos.id = %(id)s
                ;"""
        results = connectToMySQL(cls.DB).query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row_from_db["id"],
                "dojo_id" : row_from_db["dojo_id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            dojo.ninjas.append( ninja_class.Ninja( ninja_data ) )
            print(ninja_data)
        return dojo
    
    @classmethod
    def get_dojos_with_ninjas(cls):
        query = """SELECT * FROM dojos 
                LEFT JOIN ninjas  
                ON ninjas.dojo_id = dojos.id 
                ;"""
        results = connectToMySQL(cls.DB).query_db( query ) 
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["id"],
                "dojo_id" : row_from_db["dojo_id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            dojo.ninjas.append( ninja_class.Ninja( ninja_data ) )
            print(ninja_data)
        return dojo
    
    
    
    
    
    #DELETE 
    @classmethod
    def delete_dojo(cls, data):
        query = """
                DELETE FROM dojos
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results