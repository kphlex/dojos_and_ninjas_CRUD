from flask_app import app
from flask_app.controllers import ninja_routes
from flask_app.controllers import dojo_routes
from flask_app.controllers import nav_routes



if __name__ == '__main__':
    app.run(debug=True)