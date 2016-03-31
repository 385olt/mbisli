# coding=utf-8

from flask import render_template, flash, redirect, g
from app import app
from .models import getThoughts, getDate, getImage

@app.route('/')
@app.route('/index')
def index():
	dateString, month, day = getDate()
	image = getImage(month, day)
	content = getThoughts(month, day)
	return render_template('index.html', content=content, date=dateString, image=str(image))