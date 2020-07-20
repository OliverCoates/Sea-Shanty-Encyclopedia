import os
from flask import Flask
from flask  import render_template
from flask import request
from flask import redirect
from flask import session
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "SeaShantyDatabase.db"))
app = Flask(__name__)
app.secret_key = "Oh for just one time I would take the Northwest passage"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Country(db.Model):
    __tablename__ = 'Countries'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False, unique=True)



class Language(db.Model):
    __tablename__ = 'Language'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, unique=True)



class Seashanty(db.Model):
    __tablename__ = 'seashanties'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text,)
    Alternative_Names = db.Column(db.Text)
    Country_Origin = db.Column(db.ForeignKey('Countries.Name'))
    Language = db.Column(db.ForeignKey('Language.Name'))
    Description = db.Column(db.Text)
    Lyrics = db.Column(db.Text)
    AudioSource = db.Column(db.Text)

    Country = db.relationship('Country', primaryjoin='Seashanty.Country_Origin == Country.Name', backref='seashanties')
    Language1 = db.relationship('Language', primaryjoin='Seashanty.Language == Language.Name', backref='seashanties')



#t_sqlite_sequence = db.Table(
#    'sqlite_sequence',
#    db.Column('name', db.NullType),
#    db.Column('seq', db.NullType)
#)



print("")
print("Database Sucessfully loaded.")
print("")

@app.route('/', methods=["GET","POST"])
def home():
    shantys = None
    # For adding shanty
    if request.method == "POST" and request.form:
        print("! Attempting to add shanty")
        shanty = Seashanty(
            Name=request.form.get("new_name"),
            Alternative_Names=request.form.get("new_altName"),
            Description=request.form.get("new_description"),
            Country_Origin=request.form.get("new_country"),
            Language=request.form.get("new_language"),
            AudioSource=request.form.get("new_audioSource"),
            Lyrics=request.form.get("new_lyrics")
        )  # Get the data from the database and add them to the seashanties class
        db.session.add(shanty)
        db.session.commit()
        return redirect("/")
    return render_template("home.html", shantys = Seashanty.query.all())  # Return the html template

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        if 'Test' == request.form['input']:
            session['admin'] = 'yes'
            return redirect("/")
        return render_template("login.html")
    return render_template("login.html")

@app.route('/logout', methods=["GET","POST"])
def logout():
    session['admin'] = "no"
    return redirect("/")

@app.route('/update', methods=["GET","POST"])
def update():
    session['update'] = request.form.get("update_name")
    return render_template("update.html", shantys = Seashanty.query.filter(Seashanty.Name == session['update']))

@app.route('/finishUpdate', methods=["GET","POST"])
def finishUpdate():
    updated_name = request.form.get("updated_name")
    updated_altNames = request.form.get("updated_altNames")
    updated_country = request.form.get("updated_country")
    updated_language = request.form.get("updated_language")
    updated_description = request.form.get("updated_description")
    updated_lyrics = request.form.get("updated_lyrics")
    updated_audiosource = request.form.get("updated_audioSource")

    shanty = Seashanty.query.filter(Seashanty.Name == session['update']).first() # Get the name of the shanty that is being updated

    shanty.Name = updated_name
    shanty.Alternative_Names = updated_altNames
    shanty.Country_origin = updated_country
    shanty.Language = updated_language
    shanty.Description = updated_description
    shanty.Lyrics = updated_lyrics
    shanty.AudioSource = updated_audiosource

    db.session.commit()
    return redirect("/")

@app.route('/delete', methods=["POST"])
def delete():
    name = request.form.get("delete_country")
    toDelete = Seashanty.query.filter_by(Name=name).first()
    db.session.delete(toDelete)
    db.session.commit()
    return redirect("/")

@app.route('/gotoShanty', methods=["GET","POST"])
def gotoShanty():
    return render_template("home.html", shantys = Seashanty.query.all())  # Return the html template

@app.route('/gotoInfo', methods=["GET","POST"])
def gotoInfo():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug=True)
