import random
import os
import time

INVENTORY_FILE = "inventory.txt"
LEADERBOARD_FILE = "leaderboard.txt"

def save_to_file(filename, data,mode = "a"):
    """save data to file """
    with open(filename, mode)as file:
        file.write(data + "\n")

def explore_location():
    """explore a random location and find treasure."""
    location = ["mysterious cave", "haunted forest", "deserted beach", "ancinet ruins"]
    treasures = ["goldeb crown", "silver sword", "diamond necklance", "ancient artifact"]

    location = random.choice(location)
    treasure = random.choice(treasures)
    
    print("f\n exploring{location}...")
    time.sleep(2)
    print(f"you found a {treasures}!")

    save_to_file(INVENTORY_FILE, treasure)
    return treasure
def load_from_file(filename):
    """load data from a file"""
    if not os.path.exists(filename):
        return[]
    with open(filenmae, "r") as file:
        return [line.strip() for line in file]

def display_inventory():
    """display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\n leaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\n no entries in the leaderboard yet.")

def update_leaderboard(player_name, score):
    """update the leaderboard."""
    save_to_file(LEADERBOARD_FILE, f"{player_name}: {score}")
    
def treasure_hunt():
    print("welcome to treasure hunt!")
    player_name = input("enter your name: ").strip()

    #load inventory if its exist
    if os.path.exists(INVENTORY_FILE):
        print("\nresuming your adventure...")
    else:
        print("\nstarting new adventure...")
        open(INVENTORY_FILE, "w").close() #create an empty inventory file
        score = 0
    while True:
        print("\n what would you like to do?")
        print("1. expore a new location")
        print("2. view inventory")
        print("3. quit and save progress")
        choice = input("enter your choice (1/2/3): ").strip()

        if choice == "1":
            treasure = explore_location()
            score += 1
            print(f"you added {treasure} to your inventory!")
        elif choice == "2":  
            display_inventory()
        elif choice == "2":  
            print(f"\n thanks for playing, {player_name}!")
            print(f"you collected {score} tresures.")
            update_leaderboard(player_name, score)
            break
        else:
            print("invalid choice. please try again.")

def display_leaderboard():
    """display the leaderboard"""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nlearderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\n no entries in the leaderboard yet.")

def view_leaderboard():
    print("\n== leaderboard ==")
    display_leaderboard

def main():
    while True:
        print("\n== treasure hunt menu ==")
        print("1. start/resume game")
        print("2. view leaderboard")
        print("3. exit")
        choice = input ("enter your choice (1/2/3): ").strip()

        if choice == "1":
            treasure_hunt()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
            print("goodbye!")
            break
        else:
            print("invalid choice. please try again.")

if __name__ == "__main__":
    main()


