class GuessingNumberGame:

    random_number: int
    attempts: int = 0

    def __init__(self, random_number_generator: int):
        self.random_number = random_number_generator

    def guess_number(self, guessed_number: int) -> str:
        self.attempts += 1

        if guessed_number == self.random_number:
            return "Correct you won"

        if self.attempts == 3:
            return "You lose"

        if guessed_number < self.random_number:
            return "The number is higher"
        if guessed_number > self.random_number:
            return "The number is lower"
