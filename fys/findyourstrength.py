import sqlite3,json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import BibleParser,search,pickle
import os.path
DATABASE = 'fys.db'
DEBUG = True
SECRET_KEY = 'dev key'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_entry():
	verses = []
	if os.path.isfile('bible_data.pkl'):
	    with open('bible_data.pkl','rb') as inp:
	        bible = pickle.load(inp)
	    print("Loaded")
	else:
	    bible = BibleParser.getParsedContent()
	verses = search.search(bible)
	#bible.printBible()
	#Do some processing here
	return render_template('show_verses.html',verses=verses)

@app.route('/about')
def show_about():
	return render_template('about.html')

@app.route('/add_input', methods=['POST'])
def add_input():
	print(request.form['inputKey'])

	#Call scripts some processing and return to show_entry
	return redirect(url_for('show_entry'))

@app.route('/test')
def testText():
	return "Hello World"
if __name__=='__main__':
	app.run()
