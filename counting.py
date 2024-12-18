# counting fuel cells concept: loop, lists, operators
batteries = [50, 30, 4, 45, 12,18, 30]

minimum_battery_power = 20 #battery use minimum 20% charge

usable_battery_power = 0 #battery 0 power 0
usable_battery_count = 0 # usable battery 0
for battery in batteries: #check every battery
    if battery > minimum_battery_power:#check if battery is over cjarge 20% to use
        usable_battery_power += battery#if yes use power added
        usable_battery_count += 1 #if yes use battery count add
    
print(usable_battery_power, usable_battery_count)

alien_message = " hi human how are you"
print(alien_message[::-1])#to reverse


alien_message = "uoy era woh namuh ih"
print(f"""
alien_message = {alien_message}
now human message = {alien_message[::-1]}""")

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
    "you",
    "wr",
    
]
available_crews = 4
each_crew_foods = len(available_foods) // available_crews
remaining_foods_count = len(available_foods) % available_crews

print(f"each crew get {each_crew_foods} food and remaining foods count = {remaining_foods_count}")