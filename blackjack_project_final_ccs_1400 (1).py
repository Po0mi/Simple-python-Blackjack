import tkinter as tk
from tkinter import messagebox
import random

# Define variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# Dealer's name
Dealer = 'BOGART THE DESTROYER'

# Initialize chips and cheats
class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
        self.cheat = 900

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def cheats_active(self):
        self.total = self.cheat + self.total

chips = Chips()


# Define card, deck, and hand classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Function for starting the game
def start_game():
    global player_name, game_on, cheat, chips

    # Initialize game state
    game_on = True
    chips.total = 100
    player_name = entry_name.get()

    # Start UI elements
    update_labels()

def update_labels():
    # Update labels based on game state
    label_player_chips.config(text=f"Chips: {chips.total}")
    label_game_info.config(text="Welcome to Blackjack!")
    label_player_hand.config(text="Player hand: 0")

# Create the main window
window = tk.Tk()
window.title("Blackjack Game")

# Create UI elements
label_title = tk.Label(window, text="Blackjack Game", font=("Arial", 24))
label_title.pack(pady=20)

label_player_name = tk.Label(window, text="Enter your name: ")
label_player_name.pack()

entry_name = tk.Entry(window)
entry_name.pack(pady=10)

button_start = tk.Button(window, text="Start Game", command=start_game)
button_start.pack(pady=10)

label_player_chips = tk.Label(window, text="Chips: 100", font=("Arial", 14))
label_player_chips.pack(pady=10)

label_game_info = tk.Label(window, text="Welcome to Blackjack!", font=("Arial", 14))
label_game_info.pack(pady=10)

label_player_hand = tk.Label(window, text="Player hand: 0", font=("Arial", 14))
label_player_hand.pack(pady=10)

# Main game loop
window.mainloop()
