"""The dice class."""
import random


class Dice():
    """Roll the dice."""

    @staticmethod
    def roll_the_dice():
        """Roll the dice."""
        return random.randint(1, 6)
