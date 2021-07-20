#!/usr/bin/python3
"""Entry point login app"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Main"


if __name__ == "__main__":
    app.run(debug=True)
