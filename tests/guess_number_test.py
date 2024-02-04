import unittest

from src.guess_number import GuessingNumberGame
from unittest_data_provider import data_provider


class GuessingNumberGameTest(unittest.TestCase):

    @staticmethod
    def correct_guessed_number_provider():
        return (
            (5, 5),
            (4, 4),
            (3, 3),
        )

    @data_provider(correct_guessed_number_provider)
    def test_returns_you_won_when_number_generated_is_guessed_number(self, random_number, guessed_number):
        guess_number = GuessingNumberGame(random_number)

        first_attempt = guess_number.guess_number(guessed_number)

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

    @staticmethod
    def high_guessed_number_provider():
        return (
            (10, ),
            (9, ),
            (8, ),
        )

    @data_provider(high_guessed_number_provider)
    def test_returns_the_number_is_lower_when_number_generated_is_five_and_guessed_number_is_higher(self, guessed_number):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(guessed_number)

        self.assertEqual(first_attempt, "The number is lower")
