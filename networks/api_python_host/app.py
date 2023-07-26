from pathlib import Path
import flask
import requests
import sqlite3 as sqlite


path_database = Path("api_python_host", "database.db")

DATABASE = sqlite.connect(path_database)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def index():
    data = requests.get("https://randomuser.me/api")

    DATABASE.cursor()

    DATABASE.execute(
        """--sql
    CREATE TABLE IF NOT EXISTS users(
                     id int NOT NULL AUTO_INCREMENT,
                     name VARCHAR(255), 

    )
                     
"""
    )

    return data.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
