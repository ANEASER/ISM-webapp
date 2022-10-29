from enum import unique
from flask import Flask, render_template
from numpy import unicode_

from flask_sqlalchemy import SQLAlchemy

#....................................
from werkzeug.utils import secure_filename



app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usersphoto.db"
app.config['SECRET_KEY'] = "d6aac39da3ae28912e1f10b0"



db = SQLAlchemy(app)

from ourapp import route




