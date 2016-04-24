# coding=utf-8

from flask import render_template, flash, redirect, g
import html2text
from app import app
from .models import getThoughts, getDate, getImage

@app.route('/callback', methods=['GET'])
def callback():
	print(request.args.get('oauth_verifier') + " | my test ", file=sys.stderr)
	return ''

@app.route('/')
@app.route('/index')
def index():
	dateString, month, day = getDate()
	image = getImage(month, day)
	content = getThoughts(month, day)
	content_nohtml = html2text.html2text(content)
	content_nohtml = content_nohtml.replace('\n', '\\n')
	return render_template('index.html', content_nohtml=content_nohtml, content=content, date=dateString, image=str(image))