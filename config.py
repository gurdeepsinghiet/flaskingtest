from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '6565hhgrrerre=='
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/testingflaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)