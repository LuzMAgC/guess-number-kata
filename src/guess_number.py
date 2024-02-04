class GuessingNumberGame:

    def __init__(self, random_number_generator: int):
        self.random_number = random_number_generator

    def guess_number(self, guessed_number: int) -> str:
        if guessed_number == 1:
            return "The number is higher"
        return "Correct you won"
