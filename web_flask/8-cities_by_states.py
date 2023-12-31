#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/cities_by_states/", strict_slashes=False)
def states_cities_by_states():
    """
    display a HTML page.
    """
    st = storage.all("State")
    """st = [s for s in storage.all("State").values()]"""
    return render_template("8-cities_by_states.html", states=st)


@app.teardown_appcontext
def teardown_cntxt(exception):
    """
    teardown SQLAlchemy.
    """
    storage.close()


if __name__ == "__main__":
    """Your web application must be listening on 0.0.0.0
    """
    app.run(host="0.0.0.0")
