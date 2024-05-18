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
    """Displays 'Python is' followed by the value of the text variable."""
    return f"Python is {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays '<n> is a number' only if <n> is an integer."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
