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
    # players = storage.all(Player).values()
    # players = sorted(players, key=lambda k: (k.first_name, k.last_name))

    # for state in states:
    #     st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

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


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)