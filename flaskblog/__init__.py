from flask import Flask 
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)
app.config['SECRET_KEY'] = '00caf1ee75cf656a5e24c2c36fc57d80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
