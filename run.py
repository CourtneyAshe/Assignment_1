from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
MENUDB = 'menu.db'

@app.route('/')
def index():

    return render_template('index.html')

