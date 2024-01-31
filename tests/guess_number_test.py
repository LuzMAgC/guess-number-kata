import unittest

from src.guess_number import GuessNumber


class GuessNumberTest(unittest.TestCase):

    def test_setup_is_working(self):
        guess_number = GuessNumber()

        self.assertTrue(guess_number.my_method())
