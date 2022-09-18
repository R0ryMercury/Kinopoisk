from flask import abort


class AuthService:
    def __init__(self, dao) -> None:
        self.dao = dao

    def create(self, user_d):
        email = user_d.get("email")
        password = user_d.get("password")
        if None in (email, password):
            abort(404)
        self.dao.create(
            {
                "email": email,
                "password": password,
            }
        )
        