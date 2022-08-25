from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app_portal = Flask(__name__)
app_portal.config.from_object(Config)
db = SQLAlchemy(app_portal)
migrate = Migrate(app_portal, db)

from portal import routes