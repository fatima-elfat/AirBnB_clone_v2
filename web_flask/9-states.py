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


@app.route('/states/', defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    display a HTML page.
    """
    is_id = 0
    st = storage.all("State")
    if id is None:
        is_id = 1
    else:
        for s in st.values():
            if s.id == id:
                is_id = 1
                break
    return render_template(
                "9-states.html",
                states=st,
                id_=id,
                is_id=is_id
                )


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
