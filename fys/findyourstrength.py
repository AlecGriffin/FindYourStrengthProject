import sqlite3,json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


DATABASE = 'fys.db'
DEBUG = True
SECRET_KEY = 'dev key'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_entry():
	return render_template('HomePage.html')

@app.route('/add_input', methods=['POST'])
def add_input():
	print request.form['inputKey']
	
	return redirect(url_for('show_entry'))

@app.route('/test')
def testText():
	return "Hello World"
if __name__=='__main__':
	app.run()
