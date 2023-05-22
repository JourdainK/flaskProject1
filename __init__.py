from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c324ddbf7dca168830a376ccc00879e8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config["SQLALCHEMY_DATABASE_URL"]="jdbc:postgresql://localhost:5432/flask_exemple"
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://postgres:mons@localhost/flask_exemple'

db = SQLAlchemy(app)

from . import routes