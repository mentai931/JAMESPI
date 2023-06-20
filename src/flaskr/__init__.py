import os
from . import db
from flask import Flask
import sqlite3

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='2922_ara_420%ara',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder for the database exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    
    #init db 
    from . import db
    db.init_app(app)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
