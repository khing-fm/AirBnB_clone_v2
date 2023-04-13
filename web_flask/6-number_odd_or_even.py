#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ print Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ print HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def C_is_fun(text):
    """ print C followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_fun(text='is cool'):
    """ print python followed by the value of the text variableB """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ print n if n is a integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ print n if n is a integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Display a HTML page only if n is an integer """
    if n % 2 == 0:
        status = "even"
    else:
        status = "odd"
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
