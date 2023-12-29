#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from web_flask import app


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    display “Hello HBNB!”.
    using the option strict_slashes=False.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display “Hello HBNB!”.
    """
    return "HBNB"


if __name__ == "__main__":
    """Your web application must be listening on 0.0.0.0
    """
    app.run(host="0.0.0.0")
