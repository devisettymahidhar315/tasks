from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/student')
def student():
    return 'This is student.'

@app.route('/staff')
def staff():
    return 'This is staff.'

@app.route('/user/<name>')
def user(name):
    if name == 'student':
        return redirect(url_for('student'))
    elif name == 'staff':
        return redirect(url_for('staff'))
    else:
        return f'Hello {name}!'

if __name__ == '__main__':
    app.run()
