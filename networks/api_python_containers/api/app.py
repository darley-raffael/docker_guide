import os
import flask
import requests
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
path_database = os.path.join(basedir, "internal.db")


app = flask.Flask(__name__)

app.config["DEBUG"] = True

app.config["SQLALCHEMY_HOST"] = "host.docker.internal"  # network internal host python
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path_database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User{self.name}"


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def index():
    data = requests.get("https://randomuser.me/api").json()

    return data


@app.route("/users", methods=["POST"])
def insert_users():
    data = requests.get("https://randomuser.me/api").json()
    username = data["results"][0]["name"]["first"]

    user = User(name=username)
    db.session.add(user)
    db.session.commit()

    return username


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
