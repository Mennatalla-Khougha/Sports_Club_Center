#!/usr/bin/python3
"""tournaments routes"""
from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import storage
from models.tournament import Tournament
from models.sport import Sport
from models.player import Player


@app_views.route('/tournaments', strict_slashes=False)
def tournaments():
    """Retrieves the list of all tournament objects"""
    tournaments = list(storage.all(Tournament).values())
    tournaments = sorted(tournaments, key=lambda k: k.date, reverse=True)
    tournaments = list(map(lambda t: t.to_dict(), tournaments))
    return jsonify(tournaments)


@app_views.route('/tournaments/<tournament_id>', strict_slashes=False)
def tournament_with_id(tournament_id):
    """Retrieves the list of all tournament objects"""
    tournament = storage.get(Tournament, tournament_id)
    if tournament:
        return jsonify(tournament.to_dict())
    abort(404)

@app_views.route('/sports/<sport_id>/tournaments', strict_slashes=False)
def tournaments_from_sport_id(sport_id):
    """Retrieves the list of all tournament objects of a Sport"""
    sport = storage.get(Sport, sport_id)
    if sport:
        tournaments = [tournament.to_dict() for tournament in sport.tournaments]
        return jsonify(tournaments)
    abort(404)

@app_views.route('/players/<player_id>/tournaments', strict_slashes=False)
def tournaments_from_player_id(player_id):
    """Retrieves the list of all tournament objects of a player"""
    player = storage.get(Player, player_id)
    if player:
        tournaments = [tournament.to_dict() for tournament in player.tournaments]
        return jsonify(tournaments)
    abort(404)