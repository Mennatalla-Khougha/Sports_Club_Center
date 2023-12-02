#!/usr/bin/python3
"""Script for the Sport model"""
from models.BaseModel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Sport(BaseModel, Base):
    """Representation of sport"""
    __tablename__ = 'sports'
    name = Column(String(50), nullable=False)
    tournaments = relationship("Tournament", backref="sport",
                               cascade="all, delete")
    players = relationship("Player",
                           back_populates="sport",
                           cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """initializes player"""
        super().__init__(*args, **kwargs)
