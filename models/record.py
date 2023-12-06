#!/usr/bin/python3
"""Script for the Record model"""
import models
from models.BaseModel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Record(BaseModel, Base):
    """Representation of Tournamet"""
    __tablename__ = 'records'
    tournament_id = Column(String(60), ForeignKey('tournaments.id'),
                           nullable=False)
    player_id = Column(String(60), ForeignKey('players.id'), nullable=False)
    matches_played = Column(Integer, default=0)
    matches_won = Column(Integer, default=0)
    matches_lost = Column(Integer, default=0)
    score = Column(Integer, default=0)

    def __init__(self, *args, **kwargs):
        """initializes record"""
        super().__init__(*args, **kwargs)
