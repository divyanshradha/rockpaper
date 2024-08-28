import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock-Paper-Scissors Game")
        self.geometry("300x200")

        # Create a label to display the result
        self.result_label = tk.Label(self, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

        # Create buttons for rock, paper, and scissors
        self.rock_button = tk.Button(self, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

    def play(self, user_choice):
        # Generate a random choice for the computer
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        # Display the result
        self.result_label.config(text=f"Computer chose {computer_choice}. {result}")

if __name__ == "__main__":
    app = RockPaperScissorsGame()
    app.mainloop()