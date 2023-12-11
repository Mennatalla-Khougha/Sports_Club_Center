#!/usr/bin/python3
"""players routes"""
from club_api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import storage
from models.player import Player
from models.sport import Sport


@app_views.route('/players', strict_slashes=False)
def players():
    """Retrieves the list of all Player objects"""
    players = list(storage.all(Player).values())
    players = sorted(players, key=lambda k: (k.first_name, k.last_name))
    players = list(map(lambda p: p.to_dict(), players))
    return jsonify(players)


@app_views.route('/players/<player_id>', strict_slashes=False)
def player_with_id(player_id):
    """Retrieves the list of all player objects"""
    player = storage.get(Player, player_id)
    if player:
        return jsonify(player.to_dict())
    abort(404)

@app_views.route('/sports/<sport_id>/players', strict_slashes=False)
def players_from_sport_id(sport_id):
    """Retrieves the list of all Player objects of a Sport"""
    sport = storage.get(Sport, sport_id)
    if sport:
        players = [player.to_dict() for player in sport.players]
        return jsonify(players)
    abort(404)