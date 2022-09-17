from project.dao.model.genre import Genre


class GenreDao:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, mid):
        return self.session.query(Genre).get(mid)

    def get_all(self):
        return self.session.query(Genre).all()