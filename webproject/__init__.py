import os
import subprocess

from flask import Flask
from flask_login import LoginManager

from webproject.modules.extensions import db, migrate
from webproject.modules.dotenv_util import initialize_dotenv


def create_app():
    
    initialize_dotenv()

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from webproject.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from webproject.routes.admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint)

    from webproject.routes.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from webproject.routes.main import main as main_blueprint

    return app
