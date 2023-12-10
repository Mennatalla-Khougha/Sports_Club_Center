#!/usr/bin/python3
from faker import Faker
import random
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from models.record import Record
from models import storage
from datetime import datetime

fake = Faker()


# players = 500
# tournaments = 60

sports = [Sport(name="Karate"),
          Sport(name="Squash"),
          Sport(name="Track & Field")
          ]
# sports = ["Karate", "Squash", "Track & Field"]
players = []
tournaments = [[], [], []]

for i in range(500):
    g = random.choice(['M', 'F'])
    first_name = fake.first_name_male()\
        if g == 'M' else fake.first_name_female()
    last_name = fake.last_name()
    birth_day = str(fake.date_of_birth(minimum_age=5, maximum_age=35))
    if random.randint(1, 5) > 1:
        weight = round(random.uniform(25, 130), 2)
    else:
        weight = None
    if random.randint(1, 5) > 1:
        height = round(random.uniform(50, 200), 2)
    else:
        height = None
    address = fake.address()
    players.append(Player(first_name=first_name, last_name=last_name,
                          gender=g, birth_day=birth_day, weight=weight,
                          height=height, address=address,
                          sport_id=sports[random.randint(0, 2)].id))

storage.save()

adjectives = ['Grand', 'Elite', 'Championship',
              'Classic', 'Supreme', 'Masters', 'Global']
nouns = ['Challenge', 'Showdown', 'Cup', 'Trophy',
         'Clash', 'Competition', 'Invitational']

# start_date = datetime.strptime('2023-07-01', '%Y-%m-%d').date()
# end_date = datetime.strptime('2024-07-01', '%Y-%m-%d').date()

today = datetime.now().strftime('%Y-%m-%d')

for i in range(3):
    for j in range(60):
        tournament_name = f"{random.choice(adjectives)} \
            {random.choice(nouns)} {sports[i].name}"
        date = fake.date_time_between(start_date='-300d', end_date='+60d')
        date = date.strftime('%Y-%m-%d %H:%M')
        start = random.randint(5, 30)
        if start < 18:
            age_range = f"{start}-{start + 1}"
        elif start < 23:
            age_range = "18-23"
        else:
            age_range = "23-35"
        win_value = random.choice([0, 3, 3, 3, 5, 5])
        description = fake.paragraph(nb_sentences=5)
        tournaments[i].append(Tournament(name=tournament_name,
                                         sport_id=sports[i].id,
                                         date=date,
                                         age_range=age_range,
                                         win_value=win_value,
                                         description=description))
        for player in sports[i].players:
            if random.randint(1, 3) > 1:
                player.join_tournament(tournaments[i][j])
        tournaments[i][j].initial_records()
        if (date < today):
            for player in tournaments[i][j].players:
                for k in range(random.randint(3, 12)):
                    tournaments[i][j].update_records(
                        player.id,
                        random.choice([True, False])
                        )

storage.save()
