from project.dao.auth import AuthDao
from project.dao.director import DirectorDao
from project.dao.movie import MovieDao
from project.dao.genre import GenreDao
from project.services.auth import AuthService
from project.services.director import DirectorService
from project.services.genre import GenreService
from project.services.movie import MovieService
from project.setup_db import db

# DAO
director_dao = DirectorDao(db.session)
movie_dao = MovieDao(db.session)
genre_dao = GenreDao(db.session)
auth_dao = AuthDao(db.session)

# Services
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)
auth_service = AuthService(dao=auth_dao)
