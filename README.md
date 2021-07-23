# TSP Test - Login App

A simple registration/login app that shows a welcome message and the profile picture of a registered user.
This app was developed using Python, Flask, SQLAlchemy and MySQL.

## Installation

- Make sure you have MySQL 5.7+ installed

- Clone this repository

- Create a ```venv``` in python3 running ```python3 -m venv venv```

- Run pip ```install -r requirements.txt``` to install all dependencies

- Import setup_mysql.sql to your MySQL installation to create the database and user for this app.


## Environment Variables

To run this project, you will need to add the following environment variables to your ```venv/bin/activate``` file

- ```export MYSQL_USER=tsp_user```
- ```export MYSQL_PWD=tsp_user_pwd``` 
- ```export MYSQL_HOST=localhost```
- ```export MYSQL_DB=tsp_db```
- ```export FLASK_APP="app.py"```

  Remember to deactivate your python venv after adding the environment variables and activate it again by running ```source venv/bin/activate```

> :warning: **If you don't want add all the environment variables you can run the app with:**

```
MYSQL_USER=tsp_user MYSQL_PWD=tsp_user_pwd MYSQL_HOST=localhost MYSQL_DB=tsp_db python3 ./app.py
```

## Usage/Examples

In your environment run ```flask run```

If you see the next message block, that means the app if ready for use.
```
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Go to http://127.0.0.1:5000/ and enjoy.


## Folder structure

```
├── README.md
├── app.py
├── forms
│   ├── create_account.py
│   └── login.py
├── models
│   ├── engine.py
│   └── users.py
├── requirements.txt
├── setup_mysql.sql
├── static
│   └── css
│       └── bootstrap.min.css
└── templates
    ├── create_account.html
    ├── index.html
    └── login.html
```

## Pending

- User management module
- Recover password module
- Validate strong password (Just add a regex to validators)
- Validate if the user email is real
- Makeover
- Separate front ofr backend


## Authors

- [@wisvem](https://www.github.com/wisvem) - Wiston Venera Macías

  