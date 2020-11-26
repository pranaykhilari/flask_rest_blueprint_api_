from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from apps import app

db = SQLAlchemy(app)
marshmallow = Marshmallow(app)
