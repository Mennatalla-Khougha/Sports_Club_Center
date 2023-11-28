#!/usr/bin/python3
"""Script for the Player model"""
import models
from models.BaseModel import BaseModel, Base
from models.association import players_sports, players_tournaments
import sqlalchemy
from sqlalchemy import Column, String, CHAR, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class Player(BaseModel, Base):
    """Representation of player"""
    __tablename__ = 'players'
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(CHAR(1), nullable=False)
    birth_day = Column(String(15), nullable=False)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    address = Column(String(50), nullable=True)
    phone_number = Column(String(50), nullable=True)
    sports = relationship(
        'Sport',
        secondary=players_sports,
        back_populates='players'
        )
    tournaments = relationship(
        'Tournament',
        secondary=players_tournaments,
        back_populates='players'
        )

    def __init__(self, *args, **kwargs):
        """initializes player"""
        try:
            datetime.strptime(kwargs["birth_day"], "%Y-%m-%d")
        except Exception as e:
            kwargs["birth_day"] = None
        super().__init__(*args, **kwargs)

    def records(self, tournament):
        return [record for record in tournament.records
                if record.player_id == self.id]
