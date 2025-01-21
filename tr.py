from collections import deque
import random 

#Initialize deck of cards 
deck = deque ([f"{value} of {suit}" for value in
              ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "king", "Ace"]
              for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]])

#shuffle the deck
random.shuffle(deck)

#PLayers and their hands
player1 = []
player2 = []

# Draw 3 cards for each player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())

# display players' hands
print("Player 1's hand:")
print(player1)
print("\nPLayer 2's hand:")
print(player2)