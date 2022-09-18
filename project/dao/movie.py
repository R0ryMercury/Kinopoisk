from project.constants import MOVIES_PER_PAGE
from project.dao.model.movie import Movie


class MovieDao:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_new_on_page(self, page):
        query = self.session.query(Movie).order_by(Movie.year.desc())
        return query.limit(MOVIES_PER_PAGE).offset(MOVIES_PER_PAGE * (page - 1)).all()

    def get_new_all(self):
        return self.session.query(Movie).order_by(Movie.year.desc()).all()

    def get_on_page(self, page):
        return (
            self.session.query(Movie)
            .limit(MOVIES_PER_PAGE)
            .offset(MOVIES_PER_PAGE * (page-1))
            .all()
        )
