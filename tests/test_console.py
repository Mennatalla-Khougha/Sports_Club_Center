#!/usr/bin/python3
"""Define Unittest for console"""
from os import getenv
import sys
import unittest
from models import storage
from console import ConsoleCommand
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from unittest.mock import patch
from io import StringIO


class TestConsole_prompt(unittest.TestCase):
    """Unittest for the prompt"""

    def test_prompt(self):
        self.assertEqual(">>> ", ConsoleCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestConsole_quit(unittest.TestCase):
    """Unittest for exiting the prompt"""

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(ConsoleCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(ConsoleCommand().onecmd("EOF"))


class TestConsole_help(unittest.TestCase):
    """Unittest for exiting the prompt"""

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help help"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help create"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help show"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help destroy"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help all"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help count"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_update(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help update"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_append(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help append"))
            self.assertLess(5, len(output.getvalue().strip()))

    def test_no_arg(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd("help"))
            self.assertLess(5, len(output.getvalue().strip()))


class TestConsole_Create(unittest.TestCase):
    """Unittest for create method from the console"""
    def test_create_player(self):
        """test create player"""
        args = 'create Player {"first_name": "Menna",\
            "last_name": "Khougha", "gender": "F",\
                "birth_day": "1990-10-23"}'

        with patch('builtins.input', return_value='n'):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(ConsoleCommand().onecmd(args))
                id_1 = output.getvalue().strip()
                self.assertIsNotNone(storage.get(Player, id_1))

    def test_create_sport(self):
        """test create sport"""
        args = 'create Sport {"name": "Karate"}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            self.assertIsNotNone(storage.get(Sport, id_1))

    def test_create_tournament(self):
        """test create tournament"""
        sport = list(storage.all(Sport).values())[-1]
        args = f'create Tournament {{"name": "Grand_master",\
            "date": "2023-12-9 10:30", "age_range": "19-23",\
                "sport_id": "{sport.id}"}}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            self.assertIsNotNone(storage.get(Tournament, id_1))


class TestConsole_show(unittest.TestCase):
    """Unittest for show method from the console"""
    def test_show_player(self):
        """test show player"""
        args = 'create Player {"first_name": "Youmna",\
            "last_name": "Youssef", "gender": "F",\
                "birth_day": "1990-10-23"}'
        with patch('builtins.input', return_value='n'):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(ConsoleCommand().onecmd(args))
                id_1 = output.getvalue().strip()
                self.assertIsNotNone(storage.get(Player, id_1))
                self.assertFalse(ConsoleCommand()\
                    .onecmd(f"show Player {id_1}"))
                self.assertIn(id_1, output.getvalue())

    def test_show_sport(self):
        """test show sport"""
        args = 'create Sport {"name": "Squash"}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            self.assertIsNotNone(storage.get(Sport, id_1))
            self.assertFalse(ConsoleCommand()\
                .onecmd(f"show Sport {id_1}"))
            self.assertIn(id_1, output.getvalue())

    def test_show_tournment(self):
        """test show tournament"""
        sport = list(storage.all(Sport).values())[-1]
        args = f'create Tournament {{"name": "Elite_Showdown",\
            "date": "2023-12-9 10:30", "age_range": "19-23",\
                "sport_id": "{sport.id}"}}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            self.assertIsNotNone(storage.get(Tournament, id_1))
            self.assertFalse(ConsoleCommand()\
                .onecmd(f"show Tournament {id_1}"))
            self.assertIn(id_1, output.getvalue())


class TestConsole_destroy(unittest.TestCase):
    """Unittest for destroy method from the console"""
    def test_destroy_player(self):
        """test destroy player"""
        args = 'create Player {"first_name": "George",\
            "last_name": "Rafaat", "gender": "M",\
                "birth_day": "2004-9-29"}'
        with patch('builtins.input', return_value='n'):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(ConsoleCommand().onecmd(args))
                id_1 = output.getvalue().strip()
                self.assertIsNotNone(storage.get(Player, id_1))
                self.assertFalse(ConsoleCommand().onecmd(f"destroy Player {id_1}"))
                self.assertIsNone(storage.get(Player, id_1))

    def test_destroy_sport(self):
        """test destroy sport"""
        args = 'create Sport {"name": "Track & Field"}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            self.assertIsNotNone(storage.get(Sport, id_1))
            self.assertFalse(ConsoleCommand().onecmd(f"destroy Sport {id_1}"))
            self.assertIsNone(storage.get(Sport, id_1))

    def test_destroy_tournment(self):
        """test destroy tournament"""
        sport = list(storage.all(Sport).values())[-1]
        args = f'create Tournament {{"name": "Elite_masters",\
            "date": "2023-12-9 10:30", "age_range": "19-23",\
                "sport_id": "{sport.id}"}}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            self.assertIsNotNone(storage.get(Tournament, id_1))
            self.assertFalse(ConsoleCommand()\
                .onecmd(f"destroy Tournament {id_1}"))
            self.assertIsNone(storage.get(sport, id_1))


class TestConsole_update(unittest.TestCase):
    """Unittest for update method from the console"""
    def test_update_player(self):
        """test update player"""
        args = 'create Player {"first_name": "George",\
            "last_name": "Rafaat", "gender": "M",\
                "birth_day": "2004-9-29"}'
        with patch('builtins.input', return_value='n'):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(ConsoleCommand().onecmd(args))
                id_1 = output.getvalue().strip()
                update = f'update Player {id_1} {{"first_name": "new_name"}}'
                self.assertFalse(ConsoleCommand().onecmd(update))
                self.assertEqual("new_name", storage.get(Player, id_1).first_name)

    def test_update_sport(self):
        """test update sport"""
        args = 'create Sport {"name": "Track & Field"}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            update = f'update Sport {id_1} {{"name": "karate"}}'
            self.assertFalse(ConsoleCommand().onecmd(update))
            self.assertEqual("karate", storage.get(Sport, id_1).name)

    def test_update_tournment(self):
        """test update tournament"""
        sport = list(storage.all(Sport).values())[-1]
        args = f'create Tournament {{"name": "Elite_masters",\
            "date": "2023-12-9 10:30", "age_range": "19-23",\
                "sport_id": "{sport.id}"}}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(ConsoleCommand().onecmd(args))
            id_1 = output.getvalue().strip()
            update = f'update Tournament {id_1} {{"name": "new_name", "win_value": 5}}'
            self.assertFalse(ConsoleCommand().onecmd(update))
            self.assertEqual("new_name", storage.get(Tournament, id_1).name)
            self.assertEqual(5, storage.get(Tournament, id_1).win_value)


class TestConsole_append(unittest.TestCase):
    """Unittest for append method from the console"""
    def test_append_Sport(self):
        """test append player"""
        sport = list(storage.all(Sport).values())[-1]
        args = 'create Player {"first_name": "George",\
            "last_name": "Rafaat", "gender": "M",\
                "birth_day": "2004-9-29"}'
        with patch('builtins.input', return_value='n'):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(ConsoleCommand().onecmd(args))
                id_1 = output.getvalue().strip()
                player = storage.get(Player, id_1)
                self.assertEqual(0, len(player.sports))
                append = f'append {id_1} Sport {sport.id}'
                self.assertFalse(ConsoleCommand().onecmd(append))
                self.assertEqual(1, len(player.sports))
                self.assertEqual(sport, player.sports[0])

    def test_append_Tournament(self):
        """test append player"""
        tournament = list(storage.all(Tournament).values())[-1]
        args = 'create Player {"first_name": "George",\
            "last_name": "Rafaat", "gender": "M",\
                "birth_day": "2004-9-29"}'
        with patch('builtins.input', return_value='n'):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(ConsoleCommand().onecmd(args))
                id_1 = output.getvalue().strip()
                player = storage.get(Player, id_1)
                for sport in storage.all(Sport).values():
                    append = f'append {id_1} Sport {sport.id}'
                    self.assertFalse(ConsoleCommand().onecmd(append))
                self.assertEqual(0, len(player.tournaments))
                append = f'append {id_1} Tournament {tournament.id}'
                self.assertFalse(ConsoleCommand().onecmd(append))
                self.assertEqual(1, len(player.tournaments))
                self.assertEqual(tournament, player.tournaments[0])
