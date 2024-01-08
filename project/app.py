from flask import Flask, render_template, Blueprint, request, url_for, redirect
from db.logindb import logindb
from db.listdb import listdb
from db.writedb import writedb

app = Flask(__name__)
app.register_blueprint(logindb)
app.register_blueprint(listdb)
app.register_blueprint(writedb)

app.secret_key="asdasd"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/list")
def list():
    return render_template('list.html')

@app.route("/write")
def write():
    return render_template('write.html')

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="5000" ,debug=True)