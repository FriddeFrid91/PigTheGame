"""Frame layout class."""
import tkinter as tk
from PIL import Image, ImageTk


class frame_layout:
    """Framed."""

    def __init__(self, root):
        """Frame class."""
        self.root = root
        self.root.title("Pig - The Game")
        self.root.config(bg="#efe1d4")
        self.root.geometry("400x400")

        # Create a label (no initial text, as it will be updated)
        label = tk.Label(self.root, text="", font=("Comic Sans MS", 16),
                         bg="#efe1d4")
        label.pack(pady=10)

        # Update the label with a welcome message
        label.config(text="Welcome to a game of Pig!")

        # Load the image
        image = Image.open("pigImage.png")

        # Resize the image (width, height)
        new_size = (100, 100)  # Change to desired size
        image = image.resize(new_size, Image.Resampling.LANCZOS)

        # Convert the image to a Tkinter-compatible format
        self.photo = ImageTk.PhotoImage(image)
        # Store the image as an instance variable

        # Create a label to display the image
        image_label = tk.Label(self.root, image=self.photo, bg="#efe1d4")
        image_label.pack()
