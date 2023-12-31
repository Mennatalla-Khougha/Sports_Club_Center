#!/usr/bin/python3
"""Script for the Player model"""
from models.BaseModel import BaseModel, Base
from models.association import players_tournaments
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
    records = relationship("Record", backref="player",
                           cascade="all, delete")
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

    def stats(self):
        """The player records in all competitions"""
        myStats = [0, 0, 0]
        for record in self.records:
            myStats[0] += record.score
            myStats[1] += record.matches_won
            myStats[2] += record.matches_lost
        return myStats

    def age(self, date):
        """The age of the player"""
        birth_day = datetime.strptime(self.birth_day, "%Y-%m-%d")
        player_age = date.year - birth_day.year
        
        if birth_day.month > date.month:
            player_age -= 1
        elif birth_day.month == date.month:
            if birth_day.day > date.day:
                player_age -= 1
        return player_age

    def _can_join(self, tournament):
        """Checks of the player is eligable to join a tournament"""
        if self.sport_id != tournament.sport_id:
            print(f"this player doesn't play {tournament.sport.name}")
            return False
        tournament_date = datetime.strptime(tournament.date, "%Y-%m-%d %H:%M")
        age = self.age(tournament_date)
        age_range = tournament.age_range.split('-')
        if int(age_range[0]) <= age < int(age_range[1]):
            return True
        print("this player doesn't meet the age range of the tournament")
        return False

    def join_tournament(self, tournament):
        """Joins a tournament"""
        if (self._can_join(tournament)):
            self.tournaments.append(tournament)

    def played_tournaments(self):
        """The tournament already played"""
        tournaments = []
        date = datetime.now().strftime("%Y-%m-%d")
        for tournament in self.tournaments:
            if tournament.date < date:
                tournaments.append(tournament)
        return tournaments

    def to_dict(self):
        """Json representation of the player"""
        myDict = super().to_dict()
        myDict["played_tournaments"] = len(self.played_tournaments())
        myDict["age"] = self.age(datetime.now())
        myDict["sport"] = self.sport.name
        return myDict
