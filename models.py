"""
Models module
"""

from datetime import datetime
from config import db, ma

## SQLAlchemy class definition for the data in the 'movies' table
class Movies(db.Model):
    __tablename__ = "movies"
    name=db.Column(db.String)
    year=db.Column(db.Integer)
    rating=db.Column(db.Float)
    thumbnail_url=db.Column(db.String,primary_key=True)

## Marshmallow class definition for the data in the 'movies' table
class MoviesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movies
        sqla_session = db.session
