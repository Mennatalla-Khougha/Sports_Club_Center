#!/usr/bin/python3
"""Script for the Player model"""
import models
from models.BaseModel import BaseModel, Base
from models.association import players_tournaments
import sqlalchemy
from sqlalchemy import Column, String, CHAR, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Player(BaseModel, Base):
    """Representation of player"""
    __tablename__ = 'players'
    sport_id = Column(String(60), ForeignKey('sports.id'), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(CHAR(1), nullable=False)
    birth_day = Column(String(15), nullable=False)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    address = Column(String(200), nullable=True)
    phone_number = Column(String(50), nullable=True)
    sport = relationship('Sport', back_populates='players')
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

    def records(self):
        stats = [0, 0]
        for tournament in self.tournaments:
            for record in tournament.records:
                if record.player_id == self.id:
                    stats[0] += record.matches_won
                    stats[1] += record.matches_lost
                    break
        return stats

    def _can_join(self, tournament):
        can = False
        for sport in self.sports:
            if sport.id == tournament.sport_id:
                can = True
        if not can:
            print(f"this player doesn't play {models.storage.get('Sport', tournament.sport_id).name}")
            return False
        birth_day = datetime.strptime(self.birth_day, "%Y-%m-%d")
        tournament_date = datetime.strptime(tournament.date, "%Y-%m-%d %H:%M")
        age = tournament_date.year - birth_day.year
        
        if birth_day.month > tournament_date.month:
            age -= 1
        elif birth_day.month == tournament_date.month:
            if birth_day.day > tournament_date.day:
                age -= 1
        age_range = tournament.age_range.split('-')
        if int(age_range[0]) <= age < int(age_range[1]):
            return True
        print("this player doesn't meet the age range of the tournament")
        return False

    def join_tournament(self, tournament):
        if (self._can_join(tournament)):
            self.tournaments.append(tournament)