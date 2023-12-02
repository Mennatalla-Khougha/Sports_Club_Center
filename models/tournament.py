#!/usr/bin/python3
"""Script for the Tournament model"""
import models
from models.BaseModel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.association import players_tournaments
from models.record import Record
from datetime import datetime


class Tournament(BaseModel, Base):
    """Representation of Tournamet"""
    __tablename__ = 'tournaments'
    sport_id = Column(String(60), ForeignKey('sports.id'), nullable=False)
    name = Column(String(50), nullable=False)
    date = Column(String(20), nullable=False)
    age_range = Column(String(20), nullable=False)
    discription = Column(String(200), nullable=True)
    win_value = Column(Integer, default=0)
    # draw_value = Column(Integer, default=0)
    loss_value = Column(Integer, default=0)
    records = relationship("Record", backref="tournament",
                           cascade="all, delete")
    players = relationship(
        'Player',
        secondary=players_tournaments,
        back_populates='tournaments'
        )

    def __init__(self, *args, **kwargs):
        """initializes tournament"""
        try:
            datetime.strptime(kwargs["date"], "%Y-%m-%d %H:%M")
            parts = kwargs["age_range"].split('-')
            if len(parts) == 2:
                start_age = int(parts[0])
                end_age = int(parts[1])
                if not (5 <= start_age <= end_age):
                    raise Exception
            else:
                raise Exception
        except Exception:
            kwargs["date"] = None
        super().__init__(*args, **kwargs)

    def initial_records(self):
        for player in self.players:
            record = Record(tournament_id=self.id, player_id=player.id)
            record.save()

    def update_records(self, id1, win=True):
        for record in self.records:
            if record.player_id == id1:
                record.matches_played += 1
                if win:
                    record.matches_won += 1
                    record.score += self.win_value
                else:
                    record.matches_lost += 1
                break


    def add_player(self, player):
        player.join_tournament(self)
