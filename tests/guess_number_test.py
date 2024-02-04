import unittest

from src.guess_number import GuessingNumberGame


class GuessingNumberGameTest(unittest.TestCase):

    def test_a_successful_first_attempt(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(5)

        self.assertEqual(first_attempt, "Correct you won")
