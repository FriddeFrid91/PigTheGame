import tkinter as tk
from dice import Dice

class Game:
    """Game class."""

    def __init__(self, root):
        """Initialize the game state and variables."""
        self.is_running = False
        self.score = 0
        self.level = 1
        self.root = root
        self.current_score = 0
        self.root.title("Pig - The Game")
        self.root.config(bg="#efe1d4")
        self.root.geometry("400x400")
        self.player_vs_computer()

        # Create a label (no initial text, as it will be updated)
        self.label = tk.Label(self.root, text="", font=("Comic Sans MS", 16), bg="#efe1d4")
        self.label.pack(pady=10)

        # Update the label with a welcome message
        self.label.config(text="Welcome to a game of Pig!")

    def player_vs_computer(result):
        """Player vs Computer"""
        if result == 6:
            print("Congratz, you got a 6!")

    def start_game(self):
        """Start a new game or reset the current game."""
        # Create a new window for the game
        new_window = tk.Toplevel(self.root)
        new_window.title("Game Window")
        new_window.geometry("400x400")

        # Create a label for game status
        game_label = tk.Label(new_window, text="Game has started!", font=("Arial", 16))
        game_label.pack(pady=20)

        # Create a label to display the dice roll result
        result_label = tk.Label(new_window, text="Roll the dice to see the result", font=("Arial", 14))
        result_label.pack(pady=10)

        # Create a label to display the result of the current round
        current_score_label = tk.Label(new_window, text="asda", font=("Arial", 14))
        current_score_label.pack(pady=10)

        # Function to roll the dice and update the result label
        def roll_and_display_result():
            result = Dice.roll_the_dice()  # Roll the dice
            Game.player_vs_computer(result)
            current_score = Game.handling_result_of_dice(self, result)
            result_label.config(text=f"Result: {result}")  # Update the label with the result
            current_score_label.config(text=f"Current score: {current_score}")

        # Create a button to roll the dice
        roll_dice_button = tk.Button(new_window, text="Roll the dice", command=roll_and_display_result)
        roll_dice_button.pack(pady=10)
 
    def handling_result_of_dice(self, result):
        self.score += result
        return self.score

    def end_game(self):
        """End the current game."""
        self.is_running = False
        print("Game ended!")
        # Add logic to save score, handle end of game, etc.

    def reset_game(self):
        """Reset the game state."""
        self.score = 0
        self.level = 1
        print("Game reset!")
        # Reset any game-specific variables

    def increase_score(self):
        """Method to increase the game score."""
        if self.is_running:
            self.score += 10
            print(f"Score increased! Current score: {self.score}")
        else:
            print("Game is not running!")

    def next_level(self):
        """Progress to the next level."""
        if self.is_running:
            self.level += 1
            print(f"Level up! Now on level {self.level}")
        else:
            print("Game is not running!")
