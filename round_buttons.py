import tkinter as tk
from Game import Game  # Import the Game class from the Game module
from dice import Dice

class RoundButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Round Buttons Example")
        
        # Create an instance of the Game class, pass the root window
        self.game = Game(self.root)

        # Create a Canvas
        self.canvas = tk.Canvas(self.root, width=400, height=200)
        self.canvas.pack()

        # Create three wider round buttons on the canvas by adjusting the x-coordinates
        self.button1 = self.canvas.create_oval(50, 50, 150, 100, fill="pink", outline="pink", width=2)
        self.button1_text = self.canvas.create_text(100, 75, text="New Game", font=("Arial", 14), fill="white")

        self.button2 = self.canvas.create_oval(160, 50, 260, 100, fill="pink", outline="pink", width=2)
        self.button2_text = self.canvas.create_text(210, 75, text="Options", font=("Arial", 14), fill="white")

        self.button3 = self.canvas.create_oval(270, 50, 370, 100, fill="pink", outline="pink", width=2)
        self.button3_text = self.canvas.create_text(320, 75, text="Exit", font=("Arial", 14), fill="white")

        # Bind both the ovals and text to the click event
        self.canvas.tag_bind(self.button1, "<Button-1>", lambda event: self.button_click(1))
        self.canvas.tag_bind(self.button1_text, "<Button-1>", lambda event: self.button_click(1))
        self.canvas.tag_bind(self.button2, "<Button-1>", lambda event: self.button_click(2))
        self.canvas.tag_bind(self.button2_text, "<Button-1>", lambda event: self.button_click(2))
        self.canvas.tag_bind(self.button3, "<Button-1>", lambda event: self.button_click(3))
        self.canvas.tag_bind(self.button3_text, "<Button-1>", lambda event: self.button_click(3))

    # Function to handle button clicks
    def button_click(self, btn_id):
        if btn_id == 1:
            self.action_for_button1()  # Start new game
        elif btn_id == 2:
            self.action_for_button2()  # Open options window
        elif btn_id == 3:
            self.action_for_button3()  # Quit application

    # Action for Button 1 (New Game)
    def action_for_button1(self):
        print("New Game started!")
        self.game.start_game()  # Start the game using the Game instance

    # Action for Button 2 (Options)
    def action_for_button2(self):
        print("Options selected!")
        self.open_options_window()

    # Action for Button 3 (Exit)
    def action_for_button3(self):
        print("Exiting application!")
        self.root.quit()

    # Example of opening options window
    def open_options_window(self):
        options_window = tk.Toplevel(self.root)
        options_window.title("Options")
        options_window.geometry("300x200")

        label = tk.Label(options_window, text="Options Menu", font=("Arial", 16))
        label.pack(pady=20)

        # Add options (e.g., toggle sound, change difficulty, etc.)
        sound_button = tk.Checkbutton(options_window, text="Sound", onvalue=1, offvalue=0)
        sound_button.pack(pady=10)

        difficulty_label = tk.Label(options_window, text="Difficulty:")
        difficulty_label.pack()

        difficulty = tk.StringVar(value="Normal")
        difficulty_menu = tk.OptionMenu(options_window, difficulty, "Easy", "Normal", "Hard")
        difficulty_menu.pack(pady=5)
