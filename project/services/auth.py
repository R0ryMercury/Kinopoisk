from flask import abort
from loguru import logger
from project.dao.auth import AuthDao
from project.helpers import (
    check_password,
    encode_token,
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
        if user_d := encode_token(tokens.get("refresh_token")):
            return generate_tokens(user_d)
        abort(404)

    def get_info(self, token):
        if user_d := encode_token(token):
            return self.dao.get_user(user_d)
        abort(404)

    def patch(self, token, user_d):
        user = self.get_info(token)

        if name := user_d.get("name"):
            user.name = name
        if surname := user_d.get("surname"):
            user.surname = surname
        if favorite_genre := user_d.get("favorite_genre"):
            user.favorite_genre = favorite_genre

        self.dao.update(user)

    def update_pass(self, token, old_pass, new_pass):
        user = self.get_info(token)
        if not check_password(old_pass, user.password):
            abort(401)
        user.password = get_hashed_password(new_pass)
        self.dao.update(user)
