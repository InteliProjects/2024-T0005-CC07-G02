from flask import Flask
import logging
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# for password hashing
from flask_bcrypt import Bcrypt
import jwt
from src.middlewares.auth_middleware import Auth_Middleware

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# calling the dev configuration
config = Config().dev_config

# making our application to use dev env
app.env = config.ENV

# load the secret key from the environment variable
app.secret_key = os.environ.get('SECRET_KEY')
bcrypt = Bcrypt(app)

# Path for our local sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# To specify to track modifications of objects and emit signals
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

# sql alchemy instance
db = SQLAlchemy(app)

# Flask Migrate instance to handle database migrations
migrate = Migrate(app, db)

# import api blueprint to register it with the app
from src.routes import api
app.register_blueprint(api, url_prefix="/api")