from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
MENUDB = 'menu.db'

@app.route('/')
def index():

    db = sqlite3.connect(MENUDB)

    genres = []
    cur = db.execute('SELECT genre FROM Genres')
    for row in cur:
        genres.append(list(row))

    aesthetics = []
    cur = db.execute('SELECT aesthetic FROM Aesthetics')
    for row in cur:
        aesthetics.append(list(row))
    
    characters = []
    cur = db.execute('SELECT character FROM Characters')
    for row in cur:
        characters.append(list(row))

    goals = []
    cur = db.execute('SELECT goal FROM Goals')
    for row in cur:
        goals.append(list(row))

    mechanics = []
    cur = db.execute('SELECT mechanic FROM Mechanics')
    for row in cur:
        mechanics.append(list(row))

    adjectives = []
    cur = db.execute('SELECT adjective FROM Adjectives')
    for row in cur:
        adjectives.append(list(row))

    return render_template('index.html',
    genres=genres,
    adjectives=adjectives,
    aesthetics=aesthetics,
    characters=characters,
    goals=goals,
    mechanics=mechanics
    )
