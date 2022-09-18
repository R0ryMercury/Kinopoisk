from flask import request, jsonify
from flask_restx import Namespace, Resource
from project.container import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class RegisterView(Resource):
    def post(self):
        req_json = request.json
        auth_service.create(req_json)
        return "", 201


@auth_ns.route("/login")
class LoginView(Resource):
    def post(self):
        req_json = request.json
        tokens = auth_service.login(req_json)
        return jsonify(tokens)

    def put(self):
        req_json = request.json
        tokens = auth_service.new_tokens(req_json)
        return jsonify(tokens)
    