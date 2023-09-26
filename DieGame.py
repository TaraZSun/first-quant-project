import random


class Die:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return self._value


class Player:
    def __init__(self, die, counter=10, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = counter


    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter


    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1


    def roll_die(self):
        return self._die.roll()


class DiceGame:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def play(self):

    def play_round(self):
        pass
    def check_game_over(self):
        if counter == 0:
            print("Game is over!")

