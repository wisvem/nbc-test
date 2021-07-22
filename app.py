#!/usr/bin/python3
"""TSP Test - Login App"""
from flask import Flask, render_template as render
from flask import redirect, request, url_for
from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user, current_user
from forms.create_account import CreateAccountForm as caf
from forms.login import LoginForm
from models.models import User, get_user, users
from werkzeug.urls import url_parse


app = Flask(__name__)
app.config['SECRET_KEY'] = '3c314a4d0a16401e7a154afe640957c6b9f57d60d394dd6b855c90cca22a2fbc6d2c92e6f87255ce'
login_manager = LoginManager(app)
login_manager.login_view = "login"
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return render('index.html')


@app.route('/profile')
@login_required
def profile():
    return render('profile.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/create_account', methods=["GET", "POST"])
def create_account():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = caf()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        pic = form.pic.data
        # TODO database pending
        user = User(name, email, password, pic)
        users.append(user)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render('create_account.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == str(user_id):
            return user
    return None


if __name__ == "__main__":
    app.run(debug=True)
