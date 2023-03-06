from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "dn_db"
    def __init__(self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save_user(cls, data):
        query = """
                INSERT INTO users 
                (first_name, last_name, email, password, created_at, updated_at)
                VALUES 
                ( %(first_name)s, %(last_name)s , %(email)s , %(password)s , NOW() , NOW() )
                ;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s
                ;"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    #VALIDATION 
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        if len(user['email']) < 8:
            flash("Please enter a valid email address")
            is_valid = False 
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address', 'email')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters')
            is_valid = False
        return is_valid