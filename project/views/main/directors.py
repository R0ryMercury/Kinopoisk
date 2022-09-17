from flask_restx import Namespace, Resource
from project.dao.model.director import DirectorSchema
from project.container import director_service
from flask import abort

directors_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        if director := director_service.get_one(did):
            return director_schema.dump(director), 200
        abort(404)
