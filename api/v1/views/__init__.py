#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.sports import *
from api.v1.views.players import *
from api.v1.views.tournaments import *  