import random
import os
import time

INVENTORY_FILE = "inventory.txt"
PET_FILE = "pet.txt"

def save_to_file(filename, data, mode="a"):
    """Save data to a file."""
    with open(filename, mode) as file:
        file.write(data + "\n")

class Pet:
    def __init__(self, name, species, hunger=50, happiness=50,energy=50):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.name = name
        self.species = species
    def feed(self):
    print(f" the {self.name} is eating")
def play(self):
    print(f" the {self.name} is playing")
def rest(self):
    print("f{self.name} is taking rest")
def check_sickness(self):
     if self.energy<=0 or self.happiness <=0 or self.hunger<= 0:
        print(f"{self.name} is sick, Game OVERRRRRRRRR!")
        return True
        return False
def check_win(self):
    if self.energy>=80 or self.happiness>=80 or self.hunger>=80:
        print(f"{self.name} is full of happiness ang energy. so You WINNNNNNNNN!!!!!!!!")
        return True
    return False
@staticmethod
def load_from_file(filename):
    """Load data from a file."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def display_inventory():
    pet = load_from_file(PET_FILE)
    if pet:
        print("\npet:")
    for entry in pet:
        print(entry)
    else:
        print("\nNo entries in the pet_game yet.")

def update_Pet(pet_name, score):
    """Update the pet."""
    save_to_file(PET_FILE, f"{pet_name}: {score}")
        
def pet_game(Pet):
    print("Welcome to pet game!")
    pet_name = input("Enter your pet name: ").strip()
            
if os.path.exists(INVENTORY_FILE):
    print("\nResuming ...")
else: 
    print("\nStarting ...")
    open(INVENTORY_FILE, "w").close()  # Create an empty inventory file
                    
    score = 0
    while True:
        print("\nWhat would you like to do?")
        print("1. View inventory")
        print("2. Quit and save progress")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            display_inventory()
        elif choice == "2":
            print(f"\nThanks for playing, {pet_name}!")
            print(f"You collected {score} .")
            update_pet(pet_name, score)
            break
        else:
            print("Invalid choice. Please try again.")
                         
def display_Pet():
    """Display the pet."""
    Pett = load_from_file(PET_FILE)
    if Pett:
        print("\npet:")
        for entry in pet:
            print(entry)
    else:
        print("\nNo entries in the pet yet.")

def random_event(self):
        event = random.event(["toy", "accident"])
        if event == "toy":
            happiness_boost = random.randint(4, 20)
            self.happiness += happiness_boost
            print(f" {self.name} has found the toy. happiness increase by{happiness_boost} ")
        elif event == "accident":
            energy_boost = random.randint(10, 50)
            self.energy += energy_boost
            print(f"{self.name} is in accident, energy decreased by {energy_boost}")
        else:
            print(f"{self.name} did not experienxce any event today")
    

def view_Pet():
    print("\n== pet  ==")
    display_pet()
    print(f"plz choose the action for your pet")
    print(f" 1. feed")
    print(f"2. play")
    print(f" 3. rest ")
    start_time = time.time()
    p = none
    while True:
        if time.time() - start_time()> timeout:
            print(f"time out")
            print(f"the pet wil be in rest default")
            self.rest()
            p = input("enter the number of your choice ")
        if p=="1":
            Pet.feed()
        elif p=="2":
            Pet.play()
        elif p=="3":
            Pet.rest()
        else:
            print(f"error !!! plzzz choose the number correct btw 1,2 or 3: ")
            return False
def main():
    while True:
        print("\n== pet ==")
        print("1. Start/Resume Game")
        print("2. View pet")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            pet_game()
        elif choice == "2":
            view_pet()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
    
        
if __name__ == "__Pet__":
    Pet()




