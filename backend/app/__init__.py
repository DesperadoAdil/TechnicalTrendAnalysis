# -*- coding: UTF-8 -*-
from flask import Flask
from flask_session import Session

import pickle

app = Flask(__name__)
app.config.from_object('config')

Session(app)

with open("./app/cache", "rb") as f:
    cache = pickle.load(f)

from app import views, utils
