import pytest
from project.config import TestingConfig
from app import create_app, db


@pytest.fixture(scope="module")
def test_app():
    app = create_app(TestingConfig())
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
