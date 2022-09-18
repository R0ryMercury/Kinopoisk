from project.dao.movie import MovieDao


class MovieService:
    def __init__(self, dao: MovieDao) -> None:
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        status = filters.get("status")
        if page := filters.get("page"):
            page = int(page)
        if status == "new":
            if page and page > 0:
                movies = self.dao.get_new_on_page(page)
            else:
                movies = self.dao.get_new_all()
        elif page and page > 0:
            movies = self.dao.get_on_page(page)
        else:
            movies = self.dao.get_all()
        return movies
