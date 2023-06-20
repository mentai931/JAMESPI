import datetime
from flask import Blueprint, render_template, redirect, url_for, request
from flaskr.db import get_db
from flaskr.getData import getData
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():

    return "hello"

@main.route('/test')
def test():
    try:
        data = getData()
        print(data)
    
        lol = "Temperatur : {:.2f} und Feuchtigkeit: {:.2f}".format(data[0],data[1])
        #lol = f"Temperatur: {data[0]} und Feuchtigkeit: {data[1]}"
        return lol
    except:
        return "miese Briese"
