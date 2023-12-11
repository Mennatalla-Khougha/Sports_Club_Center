#!/usr/bin/python3
"""sports routes"""
from club_api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import storage
from models.sport import Sport


@app_views.route('/sports', strict_slashes=False)
def sports():
    """Retrieves the list of all sport objects"""
    sports = []
    for sport in storage.all(Sport).values():
        sports.append(sport.to_dict())
    return jsonify(sports)


@app_views.route('/sports/<sport_id>', strict_slashes=False)
def sports_with_id(sport_id):
    """Retrieves the list of all sport objects"""
    sport = storage.get(Sport, sport_id)
    if sport:
        return jsonify(sport.to_dict())
    abort(404)