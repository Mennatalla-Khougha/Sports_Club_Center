#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/club_api/v1')
from club_api.v1.views.index import *
from club_api.v1.views.sports import *
from club_api.v1.views.players import *
from club_api.v1.views.tournaments import *  