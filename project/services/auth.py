from flask import abort
from loguru import logger
from project.dao.auth import AuthDao
from project.helpers import (
    check_password,
    check_tokens,
    generate_tokens,
    get_hashed_password,
)


class AuthService:
    def __init__(self, dao: AuthDao) -> None:
        self.dao = dao

    def get_user_data(self, user_d):
        email = user_d.get("email")
        password = user_d.get("password")
        if None in (email, password):
            abort(404)
        return {
            "email": email,
            "password": password,
        }

    def create(self, data):
        user_d = self.get_user_data(data)
        user_d["password"] = get_hashed_password(user_d["password"])
        self.dao.create(user_d)

    @logger.catch
    def login(self, data):
        user_d = self.get_user_data(data)
        user = self.dao.get_user(user_d)
        if check_password(user_d.get("password"), user.password):
            return generate_tokens(user_d)
        abort(404)

    def new_tokens(self, tokens):
        if user_d := check_tokens(tokens):
            return generate_tokens(user_d)
        abort(404)
