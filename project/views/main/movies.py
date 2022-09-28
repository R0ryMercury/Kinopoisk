from flask import request, abort
from flask_restx import Namespace, Resource
from project.dao.model.movie import MovieSchema
from project.container import movie_service

movies_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page,
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200


@movies_ns.route("/<int:mid>/")
class MovieView(Resource):
    def get(self, mid):

        if movie := movie_service.get_one(mid):
            return movie_schema.dump(movie), 200

        abort(404)
