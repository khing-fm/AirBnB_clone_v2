#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

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
    """ print python followed by the value of the text variable """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
