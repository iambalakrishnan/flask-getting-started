from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my first Flask app!'

@app.route('/date')
def date():
    return 'This page was served at  date app ' + str(datetime.now())

#add a page that shows how many times the page has been visited
counter = 0

@app.route('/visits')
def count_views():
    global counter #defined outside of the function so it can be used in the function
    counter += 1
    return 'This page has been visited ' + str(counter) + ' times.'