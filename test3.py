#!/usr/bin/python3
from models import storage
from models.player import Player
from models.sport import Sport
from models.record import Record
from models.tournament import Tournament


# tournament_description = fake.paragraph(nb_sentences=3)  # Generate a paragraph of 3 sentences
# print(tournament_description)
# record = storage.get(Record, "fc09c55f-f244-4106-971e-b5d055e6e121")
# print(record.tournament)
# for tournament in storage.all(Tournament).values():
#     print(tournament.description)
#     print("_________________________________________")

# for record in storage.all(Record).values():
#     print(record.player.first_name)
#     print("_________________________________________")
# player = storage.get("Player", "9fc677d1-03d3-473b-9638-6f383ad10853")
# print([sport.name for sport in player.sports])