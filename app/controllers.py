from flask import render_template, flash, redirect, g
from app import app
from .models import getThoughts, getDate

@app.route('/')
@app.route('/index')
def index():
	dateString, month, day = getDate()
	return render_template('index.html', content=getThoughts(month, day), date=dateString)