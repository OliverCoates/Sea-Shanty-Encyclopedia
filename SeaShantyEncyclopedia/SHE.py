import os
from flask import Flask
from flask  import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "SeaShantyDatabase.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class SeaShanty(db.Model):
    ID = db.Column(db.Integer(), primary_key=True,)
    Name = db.Column(db.String(),unique=True)

print("")
print("Database Sucessfully loaded.")
print("")