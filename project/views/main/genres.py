from flask_restx import Namespace, Resource
from project.dao.model.genre import GenreSchema
from project.container import genre_service
from flask import abort

genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route("/<int:gid>/")
class GenreView(Resource):
    def get(self, gid):
        if genre := genre_service.get_one(gid):
            return genre_schema.dump(genre), 200
        abort(404)
