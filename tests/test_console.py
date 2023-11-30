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
