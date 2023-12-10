#!/usr/bin/python3
"""Script for the Tournament model"""
from models.BaseModel import BaseModel, Base
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
    description = Column(String(500), nullable=True)
    win_value = Column(Integer, default=0)
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
        """Initialize the records for all players in the beginning of the tournament"""
        for player in self.players:
            record = Record(tournament_id=self.id, player_id=player.id)
            record.save()

    def update_records(self, id1, win=True):
        """Add the played matches record"""
        record = self.get_record(id1)
        if not record:
            return
        record.matches_played += 1
        if win:
            record.matches_won += 1
            record.score += self.win_value
        else:
            record.matches_lost += 1
        record.save()


    def add_player(self, player):
        """add a player to the tournament"""
        player.join_tournament(self)

    def to_dict(self):
        """Json representation of the tournament"""
        myDict = super().to_dict()
        myDict["sport"] = self.sport.name
        return myDict

    def get_record(self, player_id):
        """Get the records of a player in this tournament"""
        for record in self.records:
            if record.player_id == player_id:
                return record
        return None
