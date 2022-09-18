from flask import Flask, render_template
from flask_restx import Api
from project.config import Config
from project.views.main.directors import directors_ns
from project.views.main.genres import genres_ns
from project.views.main.movies import movies_ns
from project.setup_db import db

# функция создания основного объекта app
def create_app(config_object):
    app = Flask(
        __name__, template_folder="project/templates", static_folder="project/static"
    )
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())


@app.route("/main/")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=10001, debug=True)