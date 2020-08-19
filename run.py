from flask import Flask, render_template, g
import sqlite3, random

app = Flask(__name__)
GENERATORDB = 'gen.db'

@app.route('/')
    
def randomiser():

    db = sqlite3.connect(GENERATORDB)

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

    Rchar = random.choice(char)
    Rchar2 = random.choice(char)

    if Rchar2 == Rchar:
        Rchar2 = random.choice(char)
    else:
        Rchar2 = Rchar2
    
    Radj = random.choice(adj)
    Radj2 = random.choice(adj)
    if Radj2 == Radj:
        Radj2 = random.choice(adj)
    else:
        Radj2 = Radj2

    Rmec = random.choice(mec)
    Rmec2 = random.choice(mec)
    if Rmec2 == Rmec:
        Rmec2 = random.choice(mec)
    else:
        Rmec2 = Rmec2


    Raes = random.choice(aes)
    Rgoal = random.choice(goal)
    Rgenre = random.choice(genre)
    
    idea = str("A " + Rgenre[0] +" Game in the style of " + Raes[0] + ", where a " + Radj[0] + " " + Rchar[0] + " uses " + Rmec[0] + " and " + Rmec2[0] + " to " + Rgoal[0] + " the " + Radj2[0] + " " + Rchar2[0] + ".")

    return render_template('index.html',
    
    idea = idea
    
    )

