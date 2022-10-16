from flask import render_template,flash,session,make_response,redirect,request
from pack import app

@app.route("/")
def homey():
    return render_template('home.html')
