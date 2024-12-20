def setup_mission():
    print("setting up for the mission ")

    available_foods = [
    "apple",
    "banana",
    "watermelon",
    "cherry",
    "kiwi",
    "chocolate",
    "orange",
    "cupcake",
    "pizza",
    ]
    available_crews = int(input("enter available crews"))
    print("setup completed")
    return available_crews, available_foods
    
    #check batteries over hundred
def get_charged_batteries():
    batteries = [50, 30, 4, 45, 12, 18, 30] ##battery basket
    minimum_battery_power = 20
    usable_battery_power = 0
    usable_battery_count = 0
    for battery in batteries:##check evry battery
        if battery > minimum_battery_power:# check if battery is over charged 20% to use
            usable_battery_power += battery# if yes use power added
            usable_battery_count = usable_battery_count + 1 #if yes use battery count add
            if usable_battery_power >= 100:
                return usable_battery_power, usable_battery_count
def decrypt_alien_message(alien_message):
    human_message = alien_message[::-1]## reverse string
    return human_message
def food_divide_equally(foods, crew_member):
    equally_foods = len(foods) // crews_numbers
    remaining_foods = len(foods) % crews_numbers
    return equally_foods, remaining_foods
    
def alien_attack_game():
    print("welcome to alien attack game")
    print("starting mission....")

    crews_number, foods = setup_mission()
    print(f"you have {crews_number} astronuts and foods available ={foods}")
    print("welcome to the mars")
    print(" your battery is dead please change the battery")
    battery_power, battery_count = get_charged_batteries()##callking the finction after it has been created

    print("hurray!! you battery is charged")
    print("oops ... alien has arrived saying:")
    print("rednerrus")
    decrypt_text = decrypt_alien_message("rednerrus")

    print(f"alien is saying: {decrypt_text}")
    print("alien has captured all astronauts")
    print("if astronanut wants escape they have divide each food and give remaining food")
    equally_divide, remaining_foods = food_divide_equally(foods, crew_number)
    print(f"you have {equally_divide} foods divide equally and remainng = {remaining_foods}")
    print("okay... now you can go to earth")
    
    print("mission completed") 
    alien_attack_game()
                

    