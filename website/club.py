#!/usr/bin/python3
""" Starts a Flash Web Application """
from os import getenv
import uuid
from models import storage
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from models.record import Record
from flask import Flask, render_template, abort
from datetime import datetime
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/club/', strict_slashes=False)
def home_page():
    """ routes the home page """
    return render_template('index.html')

@app.route('/club/players', strict_slashes=False)
def players():
    """ routes the players page """
    sports = storage.all(Sport).values()
    sports = sorted(sports, key=lambda k: k.name)

    return render_template('players.html', sports=sports)

@app.route('/club/players/<player_id>', strict_slashes=False)
def player_page(player_id):
    """ routes the player_page page """
    player = storage.get(Player, player_id)
    if not player:
        abort(404)
    stats = player.stats()
    records = sorted(player.records, key=lambda k: (-k.score, k.matches_played))
    age = player.age(datetime.now())
    return render_template('player_page.html',
                           player=player,
                           stats=stats,
                           records=records,
                           age=age)


@app.route('/club/sports', strict_slashes=False)
def sports():
    """ routes the sports page """
    return render_template('sports.html')


@app.route('/club/sports/karate', strict_slashes=False)
def karate():
    """ routes the karate page """
    return render_template('karate.html')


@app.route('/club/sports/squash', strict_slashes=False)
def squash():
    """ routes the squash page """
    return render_template('squash.html')

@app.route('/club/sports/track_field', strict_slashes=False)
def track_field():
    """ routes the track_field page """
    return render_template('track_field.html')

@app.route('/club/schedules', strict_slashes=False)
def schedules():
    """ routes the schedules page """
    return render_template('schedules.html')


@app.route('/club/tournaments', strict_slashes=False)
def tournaments():
    """ routes the tournaments page """
    sports = storage.all(Sport).values()
    sports = sorted(sports, key=lambda k: k.name)
    return render_template('tournaments.html', sports=sports)


@app.route('/club/tournaments/<tournament_id>', strict_slashes=False)
def tournament_page(tournament_id):
    """ routes the tournament_page page """
    tournament = storage.get(Tournament, tournament_id)
    if not tournament:
        abort(404)
    date = datetime.strptime(tournament.date, '%Y-%m-%d %H:%M')
    held = date < datetime.now()
    records = sorted(tournament.records, key=lambda k: (-k.score, k.matches_played))
    return render_template('tournament_page.html',
                           tournament=tournament,
                           records=records,
                           held=held)

if __name__ == "__main__":
    """ Main Function """
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', 5000)
    app.run(host=host, port=port)