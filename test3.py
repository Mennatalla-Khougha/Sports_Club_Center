#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament

for tournament in storage.all(Tournament).values():
    if (tournament.date > "2023-12-02"):
        print(tournament.age_range, tournament.date)
        print([player.birth_day for player in tournament.players])
        print("_________________________________________")

# for player in storage.all(Player).values():
#     print(player.records())
#     print("_________________________________________")
# player = storage.get("Player", "9fc677d1-03d3-473b-9638-6f383ad10853")
# print([sport.name for sport in player.sports])