# from flask import Flask, redirect, url_for, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications to reduce overhead
# db = SQLAlchemy(app)

# # Define the models for Student and Staff
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

# # class Staff(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(100), nullable=False)

# @app.route('/student')
# def student():
#     students = Student.query.all()
#     return render_template('student.html', students=students)

# # @app.route('/staff')
# # def staff():
# #     staff_members = Staff.query.all()
# #     return render_template('staff.html', staff=staff_members)

# @app.route('/user/<name>')
# def user(name):
#     if name == 'student':
#         return redirect(url_for('student'))
#     # elif name == 'staff':
#     #     return redirect(url_for('staff'))
#     else:
#         return f'Hello {name}!'

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, redirect, url_for, render_template
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications to reduce overhead
db = SQLAlchemy(app)

# Define the models for Student and Staff
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/student')
def student():
    students = Student.query.all()
    return render_template('student.html', students=students)

@app.route('/staff')
def staff():
    staff_members = Staff.query.all()
    return render_template('staff.html', staff=staff_members)

@app.route('/user/<name>')
def user(name):
    if name == 'student':
        return redirect(url_for('student'))
    elif name == 'staff':
        return redirect(url_for('staff'))
    else:
        return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True)
