# -*- coding: utf-8 -*-
from app import app
from flask import json, render_template, request
from markupsafe import escape



@app.route('/')
def index():
    return 'Hi'
    # return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

