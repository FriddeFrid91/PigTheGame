import unittest
from dice import Dice

class TestDice(unittest.TestCase):

    def test_roll_the_dice(self):
        """Testing the dice."""
        dice = Dice()  # Create a 6-sided dice instance
        value = dice.roll_the_dice()  # Roll the dice
        self.assertGreaterEqual(value, 1, "The dice roll is too low")  # Value should be >= 1
        self.assertLessEqual(value, 6, "The dice roll is too high")  # Value should be <= 6


if __name__ == "__main__":
    unittest.main()
