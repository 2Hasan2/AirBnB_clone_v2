#!/usr/bin/python3
"""This module starts a Flask web application"""
import flask

app = flask.Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
