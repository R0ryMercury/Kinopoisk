import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = "249y823r9v8238r9u"

    JSON_AS_ASCII = False
    RESTX_JSON = {
        "ensure_ascii": False,
    }

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "movies.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    