#!/usr/bin/python3
"""TSP Test - Login App"""
from flask import Flask, redirect, request, render_template as render
from flask_login import LoginManager as lm

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return render('index.html')


@app.route('/login')
def login():
    return render('/login.html')


@app.route('/create_account', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render('/create_account.html')


if __name__ == "__main__":
    app.run(debug=True)
