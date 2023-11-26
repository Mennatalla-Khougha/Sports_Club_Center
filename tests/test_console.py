#!/usr/bin/python3
"""Define Unittest for console"""
import os
import sys
import unittest
from models import storage
from console import ConsoleCommand
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


class TestConsole_player(unittest.TestCase):
    """Unittest for creating from the prompt"""
