import datetime
from flask import Blueprint, render_template, redirect, url_for, request
from flaskr.db import get_db

main = Blueprint('main', __name__)

@main.route('/index')
def index():
    return "hello"
