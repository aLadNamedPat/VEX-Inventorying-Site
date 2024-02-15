from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from sqlalchemy import create_engine, inspect
import os
import pyodbc
# init SQLAlchemy so we can use it later in our models

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    #new mysql db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{password here}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aPat0203@localhost/flasksql'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = os.urandom(12).hex()
    # engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

    #old sqlite db
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # inspector = inspect(engine)

    # # Print the table names
    # print(inspector.table_names())
    with app.app_context():
        db.create_all()
    return app
