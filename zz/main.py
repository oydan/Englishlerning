from flask import Flask, request
from flask import render_template
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def mn():
    return render_template('index.html')


@app.route('/ishak')
def details():
    return render_template('int.html')



@app.route('/lesson')
def lesson():
    return render_template('lesson.html')


@app.route('/teachers')
def teachers():
    return render_template('teach.html')


@app.route('/about')
def about():
    return render_template('abschool.html')



if __name__ == "__main__":
    app.run()