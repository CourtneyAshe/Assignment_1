from flask import Flask, render_template, g
import sqlite3, random

app = Flask(__name__)
GENERATORDB = 'gen.db'

@app.route('/')
def index():

    db = sqlite3.connect(GENERATORDB)

    #Grab random variable from each category, accessible from the index, through clicking a button.

    mec = []
    cur = db.execute('SELECT mechanic FROM Mechanics')
    for row in cur:
        mec.append(list(row))

    adj = []
    cur = db.execute('SELECT adjective FROM Adjectives')
    for row in cur:
        adj.append(list(row))

    aes = []
    cur = db.execute('SELECT aesthetic FROM Aesthetics')
    for row in cur:
        aes.append(list(row))

    goal = []
    cur = db.execute('SELECT goal FROM Goals')
    for row in cur:
        goal.append(list(row))

    char = []
    cur = db.execute('SELECT character FROM Characters')
    for row in cur:
        char.append(list(row))

    genre = []
    cur = db.execute('SELECT genre FROM Genres')
    for row in cur:
        genre.append(list(row))

    return render_template('index.html',
    adjectives=adj,
    mechanics=mec,
    aesthetics=aes,
    characters=char,
    goals=goal,
    genres=genre
    )
        
    
