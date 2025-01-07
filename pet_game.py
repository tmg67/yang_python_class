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
    def __init__(self, name, species, hunger=50, happiness=50, energy=50):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.name = name
        self.species = species

    def feed(self):
        print(f"{self.name} is eating.")
        self.hunger += 10
        self.happiness -= 5
        self.energy -= 5

    def play(self):
        print(f"{self.name} is playing.")
        self.happiness += 10
        self.energy -= 5

    def rest(self):
        print(f"{self.name} is resting.")
        self.energy += 10

    def check_sickness(self):
        if self.energy <= 0 or self.happiness <= 0 or self.hunger <= 0:
            print(f"{self.name} is sick, Game OVER!")
            return True
        return False

    def check_win(self):
        if self.energy >= 80 or self.happiness >= 80 or self.hunger >= 80:
            print(f"{self.name} is full of happiness and energy. You WIN!")
            return True
        return False

    @staticmethod
    def load_from_file(filename):
        """Load data from a file."""
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return [line.strip() for line in file]

    def display_inventory(self):
        pet_data = Pet.load_from_file(PET_FILE)
        if pet_data:
            print("\nPet Inventory:")
            for entry in pet_data:
                print(entry)
        else:
            print("\nNo entries in the pet game yet.")

    def update_pet(self, score):
        """Update the pet's information in the file."""
        save_to_file(PET_FILE, f"{self.name}: {score}")

    def random_event(self):
        event = random.choice(["toy", "accident"])
        if event == "toy":
            happiness_boost = random.randint(4, 20)
            self.happiness += happiness_boost
            print(f"{self.name} found a toy! Happiness increased by {happiness_boost}.")
        elif event == "accident":
            energy_boost = random.randint(10, 50)
            self.energy -= energy_boost
            print(f"{self.name} had an accident! Energy decreased by {energy_boost}.")
        else:
            print(f"{self.name} did not experience any event today.")

def pet_game(pet):
    print("Welcome to the pet game!")
    score = 0
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed pet")
        print("2. Play with pet")
        print("3. Rest pet")
        print("4. View inventory")
        print("5. Quit and save progress")
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.rest()
        elif choice == "4":
            pet.display_inventory()
        elif choice == "5":
            print(f"\nThanks for playing, {pet.name}!")
            print(f"You collected {score} points.")
            pet.update_pet(score)
            break
        else:
            print("Invalid choice. Please try again.")

def view_pet(pet):
    print("\n== View Pet ==")
    print(f"Pet Name: {pet.name}")
    print(f"Species: {pet.species}")
    print(f"Hunger: {pet.hunger}")
    print(f"Happiness: {pet.happiness}")
    print(f"Energy: {pet.energy}")
    print("\nChoose an action for your pet:")
    print("1. Feed")
    print("2. Play")
    print("3. Rest")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.rest()
    else:
        print("Invalid choice. Please try again.")

def main():
    pet_name = input("Enter your pet's name: ").strip()
    pet_species = input("Enter your pet's species: ").strip()
    my_pet = Pet(pet_name, pet_species)

    while True:
        print("\n== Pet Menu ==")
        print("1. Start/Resume Game")
        print("2. View Pet Status")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            pet_game(my_pet)
        elif choice == "2":
            view_pet(my_pet)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
