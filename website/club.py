#!/usr/bin/python3
""" Starts a Flash Web Application """
from os import getenv
import uuid
from models import storage
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from models.record import Record
from flask import Flask, render_template, abort, request, redirect, url_for
from flask_security import login_required
from datetime import datetime
from website.user_table import user_datastore, app, db
from flask_security.utils import hash_password
# from datetime import datetime
# app = Flask(__name__)




@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
def home_page():
    """ routes the home page """
    return render_template('index.html')

@app.route('/players', strict_slashes=False)
def players():
    """ routes the players page """
    sports = storage.all(Sport).values()
    sports = sorted(sports, key=lambda k: k.name)

    players = storage.all(Player).values()
    players = sorted(players, key=lambda k: (k.first_name, k.last_name))
    ages = [player.age(datetime.now()) for player in players]

    return render_template('players.html',
                           sports=sports, players=players, ages=ages, size=len(ages))

@app.route('/players/<player_id>', strict_slashes=False)
def player_page(player_id):
    """ routes the player_page page """
    player = storage.get(Player, player_id)
    if not player:
        abort(404)
    stats = player.records()
    age = player.age(datetime.now())
    return render_template('player_page.html',
                           player=player,
                           stats=stats,
                           age=age)


@app.route('/sports', strict_slashes=False)
def sports():
    """ routes the sports page """
    return render_template('sports.html')


@app.route('/sports/karate', strict_slashes=False)
def karate():
    """ routes the karate page """
    return render_template('karate.html')


@app.route('/sports/squash', strict_slashes=False)
def squash():
    """ routes the squash page """
    return render_template('squash.html')

@app.route('/sports/track_field', strict_slashes=False)
def track_field():
    """ routes the track_field page """
    return render_template('track_field.html')

@app.route('/schedules', strict_slashes=False)
def schedules():
    """ routes the schedules page """
    return render_template('schedules.html')

@app.route('/register', methods=['POST','GET'],strict_slashes=False)
def register():
    """routes the register page"""
    if request.method == 'POST':
        user_datastore.create_user(
            email=request.form.get('email'),
            password=hash_password(request.form.get('password'))
        )
        db.session.commit()
        
        return redirect(url_for('profile'))

    return render_template('register.html')

@app.route('/profile')
@login_required
def profile():
    """routes the profile page"""
    return render_template('profile.html')

if __name__ == "__main__":
    """ Main Function """
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port)