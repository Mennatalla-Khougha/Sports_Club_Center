#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament
from datetime import date, datetime

player1 = Player(first_name='george', last_name="raafat", gender='M',
                 birth_day=date(2004, 9, 29))
player2 = Player(first_name='manna', last_name="k", gender='F',
                 birth_day=date(1994, 5, 11))


sport1 = Sport(name='tennis')
sport2 = Sport(name='squash')

tournament_tennis = Tournament(sport_id=sport1.id, name="my tournament",
                               date=datetime(2023, 12, 15, 17, 30, 0),
                               age_range="15-20")
# Associate players with sports
player1.sports.append(sport1)
player2.sports.append(sport1)
player2.sports.append(sport2)

player1.tournaments.append(tournament_tennis)
player2.tournaments.append(tournament_tennis)

p1_sports = player1.sports
s1_players = sport1.players

records = tournament_tennis.initial_records()
player1.save()
player2.save()
sport1.save()
sport2.save()
tournament_tennis.save()

print([sport.name for sport in p1_sports])
print([player.first_name for player in s1_players])
print([player.first_name for player in tournament_tennis.players])
print(tournament_tennis.date)
print([record.to_dict() for record in records])
