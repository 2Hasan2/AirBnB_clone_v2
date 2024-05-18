#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C' followed by the value of the text variable."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return f"Python is {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
