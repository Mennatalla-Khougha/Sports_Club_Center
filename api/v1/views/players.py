#!/usr/bin/python3
"""players routes"""
from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import storage
from models.player import Player
from models.sport import Sport


@app_views.route('/players', strict_slashes=False)
def players():
    """Retrieves the list of all Player objects"""
    players = []
    for player in storage.all(Player).values():
        players.append(player.to_dict())
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
        lst = []
        for player in sport.players:
            myDict = player.to_dict()
            myDict["played_tournaments"] = player.played_tournaments()
            myDict["age"] = player.age()
            lst.append(myDict)
        return jsonify(lst)
    abort(404)