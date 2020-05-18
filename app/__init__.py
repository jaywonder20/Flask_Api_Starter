from os import path, environ
from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.utils import redirect
import logging
from flask_restful_swagger_2 import Api
from flask_swagger_ui import get_swaggerui_blueprint
import app.api_v1 as api_v1

# logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

db = SQLAlchemy()

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

swagger_ui_blueprint = get_swaggerui_blueprint(
    "/api/docs",
    "/api/swagger.json",
    config={
        'app_name': "app"
    }

)

api = Api(Blueprint('api', __name__))
migrate = Migrate(compare_type=True)

from app.database_models import *


def load_api_endpoints():
    api.add_resource(api_v1.TestEndpoint, '/test')


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    api.init_app(app)
    CORS(app)
    load_api_endpoints()

    app.register_blueprint(api.blueprint)
    app.register_blueprint(swagger_ui_blueprint, url_prefix="/api/docs")

    with app.app_context():
        db.create_all()  # Create database tables for our data models

    @app.route("/")
    def main():
        return redirect("/api/docs")

    return app
