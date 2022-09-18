from flask import request, abort
from flask_restx import Namespace, Resource
from project.container import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("register")
class RegisterView(Resource):
    def post():
        req_json = request.json
        auth_service.create(req_json)
        return "", 201
