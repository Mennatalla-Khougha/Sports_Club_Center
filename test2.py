#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament
from datetime import date, datetime

tennis = Sport(name='tennis')
squash = Sport(name='squash')

player1 = Player(first_name='george', last_name="raafat", gender='M',
                 birth_day="2004-09-29")

player1.sports.append(tennis)

print([sport.name for sport in player1.sports])

tournament_tennis = Tournament(sport_id=tennis.id, name="my tournament",
                               date="2023-12-9 10:30",
                               age_range="19-23")

tournament_tennis2 = Tournament(sport_id=tennis.id, name="my tournament2",
                               date="2023-12-9 10:30",
                               age_range="18-20")

tournament_squash = Tournament(sport_id=squash.id, name="my tournament3",
                               date="2023-12-9 10:30",
                               age_range="15-20")

player1.join_tournament(tournament_tennis)
tournament_tennis2.add_player(player1)
player1.join_tournament(tournament_squash)

print(player1.tournaments[0].name)