# -*- coding: UTF-8 -*-
from flask import *
from app import app

@app.route('/')
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return 'Hello World!'
