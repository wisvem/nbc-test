#!/usr/bin/python3
"""TSP Test - Login App"""
from flask import Flask, render_template as render
from flask import redirect, request, url_for
from flask import send_from_directory
from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user, current_user
from forms.create_account import CreateAccountForm
from forms.login import LoginForm
from models.users import User
from models.engine import db
from os.path import join, splitext
from os import makedirs, getenv
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename


usr = getenv('MYSQL_USER')
pwd = getenv('MYSQL_PWD')
host = getenv('MYSQL_HOST')
db_name = getenv('MYSQL_DB')
env = getenv('HBNB_ENV')
mysql_uri = f'mysql+pymysql://{usr}:{pwd}@{host}/{db_name}'

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = '3c314a4d0a16401e7a154afe640957c6b9f57'
app.config['UPLOAD_FOLDER'] = './data/images/'
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

login_manager = LoginManager(app)
login_manager.login_view = "login"
db.init_app(app)
with app.app_context():
    db.create_all()


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
        user = User.get_by_email(form.email.data)
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
    form = CreateAccountForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        profile_pic = form.pic.data
        user = User.get_by_email(email)
        if user:
            error = f'El {email} ya se encuentra registrado'
        else:
            user = User()
            pic_name = secure_filename(profile_pic.filename)
            pic_name = f"{user.id}{splitext(pic_name)[-1]}"
            pic_path = join(app.config['UPLOAD_FOLDER'], pic_name)
            profile_pic.save(pic_path)
            user.update(name, email, password, pic_name)
            user.save()

            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render('create_account.html', form=form, error=error)


@app.route('/data/images/<filename>')
@login_required
def user_pic(filename):
    dir_path = app.config['UPLOAD_FOLDER']
    print(dir_path)
    return send_from_directory(dir_path, filename)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


if __name__ == "__main__":
    app.run(debug=True)
