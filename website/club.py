#!/usr/bin/python3
""" Starts a Flash Web Application """
import uuid
from models import storage
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from models.record import Record
from os import environ
from flask import Flask, render_template, abort
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
# cache_id={{ cache_id }}


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

    return render_template('players.html',
                           sports=sports)

@app.route('/players/<player_id>', strict_slashes=False)
def player_page(player_id):
    """ routes the player_page page """
    player = storage.get(Player, player_id)
    if not player:
        abort(404)
    stats = player.records()
    return render_template('player_page.html',
                           player=player,
                           stats=stats)


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


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)