from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

cooking_helper = Flask(__name__)
cooking_helper.config.from_object(Config)
db = SQLAlchemy(cooking_helper)
migrate = Migrate(cooking_helper, db)

from cookinghelper import routes