#!/usr/bin/python3
from sqlalchemy import Table, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.BaseModel import Base


players_sports = Table(
    'players_sports', Base.metadata,
    Column('player_id', String(60), ForeignKey('players.id')),
    Column('sport_id', String(60), ForeignKey('sports.id'))
)


players_tournaments = Table(
    'players_tournaments', Base.metadata,
    Column('player_id', String(60), ForeignKey('players.id')),
    Column('tournament_id', String(60), ForeignKey('tournaments.id'))
)
