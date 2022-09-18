from project.dao.model.user import User


class AuthDao:
    def __init__(self, session) -> None:
        self.session = session

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
    