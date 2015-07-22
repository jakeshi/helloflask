import os
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
@app.route('/')
def hello():
    return 'Hello World!'
