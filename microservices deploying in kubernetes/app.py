from flask import Flask

app= Flask(__name__)

@app.route("/")
def jk():
    return 'please like '

if __name__=='__main__':
    app.run()
