from loguru import logger
from flask import request
from flask_restx import Namespace, Resource
from project.container import auth_service
from project.dao.model.user import UserSchema
from project.helpers import auth_required

user_ns = Namespace("user")
user_schema = UserSchema()


@user_ns.route("")
class UserView(Resource):
    @auth_required
    def get(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        user = auth_service.get_info(token)
        return user_schema.dumps(user), 200

    @auth_required
    def patch(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        auth_service.patch(token)
        return "", 204


@user_ns.route("/password")
class PasswordChangeView(Resource):
    @auth_required
    def put(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        req_json = request.json
        password_1 = req_json.get("password_1")
        password_2 = req_json.get("password_2")
        auth_service.update_pass(token, password_1, password_2)
        return "", 204
