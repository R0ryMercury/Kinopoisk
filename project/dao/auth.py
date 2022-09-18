from project.dao.model.user import User


class AuthDao:
    def __init__(self, session) -> None:
        self.session = session

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()

    def get_user(self, user_d):
        email = user_d.get("email")
        return self.session.query(User).filter(User.email == email).first()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
