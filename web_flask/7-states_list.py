#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list/', strict_slashes=False)
def states_list():
    """
    display a HTML page.
    """
    st = storage.all("State")
    return render_template('7-states_list.html', states=st)


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
