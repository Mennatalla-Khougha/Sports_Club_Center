#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament
from datetime import date, datetime

player1 = Player(first_name='george', last_name="raafat", gender='M',
                 birth_day="2004-09-29")
player2 = Player(first_name='manna', last_name="k", gender='F',
                 birth_day="2004-09-29")

x1 = Player(first_name='x1', last_name="y1", gender='F',
                 birth_day="2004-09-29")

x2 = Player(first_name='x2', last_name="y2", gender='F',
                 birth_day="2004-09-29")


tennis = Sport(name='tennis')
squash = Sport(name='squash')
karate = Sport(name='karate')

tournament_tennis = Tournament(sport_id=tennis.id, name="my tournament",
                               date="2023-12-9 10:30",
                               age_range="15-20")
tournament_tennis2 = Tournament(sport_id=tennis.id, name="my tournament2",
                               date="2023-12-9 10:30",
                               age_range="15-20")

# Associate players with sports
player1.sports.append(tennis)
player2.sports.append(tennis)
player2.sports.append(squash)
x1.sports.append(tennis)

player1.tournaments.append(tournament_tennis)
player2.tournaments.append(tournament_tennis)

tournament_tennis2.players.append(player1)

tournament_tennis.initial_records()
tournament_tennis2.initial_records()

storage.save()
