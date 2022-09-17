from project.setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    trailer = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
