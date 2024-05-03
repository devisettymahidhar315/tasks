import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)

@app.route('/')
def welcome():
    return 'Welcome to the student and staff details!'


@app.route('/student')
def student():
    return render_template('student.html', students=Student)

@app.route('/staff')
def staff():
    return render_template('staff.html', staf=Staff)

@app.route('/user/<name>')
def user(name):
    if name == 'student':
        return redirect(url_for('student'))
    elif name == 'staff':
        return redirect(url_for('staff'))
    else:
        return f'Hello {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')




