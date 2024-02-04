import unittest

from src.guess_number import GuessingNumberGame


class GuessingNumberGameTest(unittest.TestCase):

    def test_a_successful_first_attempt(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(5)

        self.assertEqual(first_attempt, "Correct you won")

    def test_returns_the_number_is_higher_when_number_generated_is_five_and_guessed_number_is_one(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(1)

        self.assertEqual(first_attempt, "The number is higher")

    def test_returns_the_number_is_higher_when_number_generated_is_five_and_guessed_number_is_two(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(2)

        self.assertEqual(first_attempt, "The number is higher")

    def test_returns_the_number_is_higher_when_number_generated_is_five_and_guessed_number_is_three(self):
        guess_number = GuessingNumberGame(5)

        first_attempt = guess_number.guess_number(3)

        self.assertEqual(first_attempt, "The number is higher")
