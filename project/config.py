import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "249y823r9v8238r9u"
    TESTING = False

    JSON_AS_ASCII = False
    RESTX_JSON = {
        "ensure_ascii": False,
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "movies.db")


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_TEST_URI = "sqlite:///" + os.path.join(
        BASEDIR, "movies_test.db"
    )
