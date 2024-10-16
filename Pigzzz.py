import tkinter as tk
from Game import Game
from frame_layout import frame_layout  # Import frame_layout
from round_buttons import RoundButtonApp  # Import RoundButtonApp

def main():
    # Create the main window
    window = tk.Tk()

    # Instantiate the frame_layout class (initializes the layout)
    layout = frame_layout(window)

    # Instantiate the RoundButtonApp class (adds round buttons)
    app = RoundButtonApp(window)

    # The button actions should be tied to events, so they will be triggered when the user interacts
    # Instead of calling them directly here, they will be activated based on UI events inside RoundButtonApp

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()


