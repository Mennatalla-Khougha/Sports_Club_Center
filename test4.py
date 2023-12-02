#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament
from datetime import date, datetime

tennis = Sport(name='tennis')
squash = Sport(name='squash')
karate = Sport(name='karate')


player1 = Player(first_name='george', last_name="raafat", gender='M',
                 birth_day="2004-09-29", sport_id=tennis.id)



player2 = Player(first_name='manna', last_name="k", gender='F',
                 birth_day="2004-09-29", sport_id=squash.id)

x1 = Player(first_name='x1', last_name="y1", gender='F',
                 birth_day="2004-09-29", sport_id=tennis.id)

x2 = Player(first_name='x2', last_name="y2", gender='F',
                 birth_day="2004-09-29", sport_id=tennis.id)

tournament_tennis = Tournament(sport_id=tennis.id, name="my tournament",
                               date="2023-12-9 10:30",
                               age_range="15-20")
tournament_tennis2 = Tournament(sport_id=tennis.id, name="my tournament2",
                               date="2023-12-9 10:30",
                               age_range="15-20")

storage.save()
print(player1.sport_id)
print(player1.sport.name)
print([player.first_name for player in tennis.players])
print([player.first_name for player in karate.players])
print("_____________________")

player1.sport = karate

storage.save()

print(player1.sport_id)
print(player1.sport.name)
print([player.first_name for player in tennis.players])
print([player.first_name for player in karate.players])

karate.delete()

print(storage.get(Player, player1.id))