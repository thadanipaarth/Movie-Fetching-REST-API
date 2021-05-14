"""
Configuration module
"""

import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir= os.path.abspath(os.path.dirname(__file__))

connex_app= connexion.App(__name__, specification_dir=basedir)

app= connex_app.app

# SqlAlchemy app configuration
sqlite_url= "sqlite:///" + os.path.join(basedir, "database.db")
app.config["SQLALCHEMY_ECHO"]= True
app.config["SQLALCHEMY_DATABASE_URI"]= sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

# Creating SqlAlchemy db instance and initializing Marshmallow
db= SQLAlchemy(app)
ma= Marshmallow(app)
