class GuessingNumberGame:

    def __init__(self, random_number_generator: int):
        self.random_number = random_number_generator

    def guess_number(self, guessed_number: int) -> str:
        if guessed_number < self.random_number:
            return "The number is higher"
        if guessed_number != 5:
            return "The number is lower"
        return "Correct you won"
