from collections import deque
import random

#initialize deck of cards
deck = deque([f"{value} of {suit}" for value in 
        ["2","3", "4","5", "6","7","8","9","10","jack", "queen","king", "ace"]
        for suit in["hearts","duamonds", "clubs","spades"]])

#shuffle the deck
random.shuffle(deck)

#players and their hands
player1 = []
player2 = []

#draw 3 cards for each players
for _ in range(3): 
    player1.append(deck.popleft())
    player2.append(deck.popleft())

#display players hands
print("player 1's hand:")
print(player1)
print("player2's hand:")
print(player2)