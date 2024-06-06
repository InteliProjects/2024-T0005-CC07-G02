from flask import Flask 
import os 
from src.config.config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_bcrypt import Bcrypt
import jwt 

load_dotenv()

app = Flask(__name__)

config = Config().dev_config

app.env = config.ENV

app.secret_key = os.environ.get('SECRET_KEY')
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from src.routes import api
app.register_blueprint(api, url_prefix='/api')
