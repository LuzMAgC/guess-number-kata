class GuessingNumberGame:

    def __init__(self, random_number_generator: int):
        self.random_number = random_number_generator

    def guess_number(self, guessed_number: int) -> str:
        return "Correct you won"
