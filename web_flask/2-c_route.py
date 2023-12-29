#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    display “C ” followed by the value of the text variable.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    """Your web application must be listening on 0.0.0.0
    """
    app.run(host="0.0.0.0")
