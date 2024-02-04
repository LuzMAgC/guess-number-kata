import unittest

from src.guess_number import GuessingNumberGame
from unittest_data_provider import data_provider


class GuessingNumberGameTest(unittest.TestCase):

    def test_a_successful_first_attempt(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(5)

        self.assertEqual(first_attempt, "Correct you won")

    @staticmethod
    def small_guessed_number_provider():
        return (
            (1, ),
            (2, ),
            (3, ),
        )

    @data_provider(small_guessed_number_provider)
    def test_returns_the_number_is_higher_when_number_generated_is_five_and_guessed_number_is_lower(self, guessed_number):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(guessed_number)

        self.assertEqual(first_attempt, "The number is higher")

    def test_returns_the_number_is_lower_when_number_generated_is_five_and_guessed_number_is_ten(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(10)

        self.assertEqual(first_attempt, "The number is lower")

    def test_returns_the_number_is_lower_when_number_generated_is_five_and_guessed_number_is_nine(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(9)

        self.assertEqual(first_attempt, "The number is lower")
