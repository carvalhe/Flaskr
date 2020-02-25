# The __init__.py serves double duty: it will contain the application factory, 
# and it tells Python that the flaskr directory should be treated as a package.

import os
from flask import Flask
from . import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # SECRET_KEY is used by Flask and extensions to keep data safe. 
    # It’s set to 'dev' to provide a convenient value during development, 
    # but it should be overridden with a random value when deploying.

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    db.init_app(app)
    
    return app