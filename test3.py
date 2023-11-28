#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament

for tournament in storage.all(Tournament).values():
    if (tournament.date > "2023-11-28"):
        print(tournament.age_range, tournament.date)
        print([player.birth_day for player in tournament.players])
        print("_________________________________________")