#!/usr/bin/python3
"""Script for the Sport model"""
import models
from models.BaseModel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.association import players_sports

class Sport(BaseModel, Base):
    """Representation of sport"""
    __tablename__ = 'sports'
    name = Column(String(50), nullable=False)
    tournaments = relationship("Tournament", backref="sport", cascade="all, delete")
    players = relationship(
        'Player',
        secondary=players_sports,
        back_populates='sports'
        )

    def __init__(self, *args, **kwargs):
        """initializes player"""
        super().__init__(*args, **kwargs)