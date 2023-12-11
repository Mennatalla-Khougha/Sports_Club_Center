#!/usr/bin/python3
"""status and stats routes"""
from club_api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """displays a API page"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ retrieves the number of each objects by type"""
    response = {
        "players": storage.count('Player'),
        "sports": storage.count('Sport'),
        "tournaments": storage.count('Tournament'),
    }
    return jsonify(response)