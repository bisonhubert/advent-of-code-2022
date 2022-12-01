INPUT_FILEPATH = './input_01.py'

def get_inventory(filepath):
    f = open(filepath)
    ration_delivery = f.readlines()
    elf_inventory = []
    inventory = []
    for ration in ration_delivery:
        if ration == '\n':
            inventory.append(elf_inventory)
            elf_inventory = []
        else:
            ration = ration[:-1] # remove newline
            ration = int(ration) # convert str to int
            elf_inventory.append(ration)
    return inventory

def get_calorie_totals(inventory):
    calorie_totals = []
    for elf_inventory in inventory:
        calorie_totals.append(sum(elf_inventory))
    return calorie_totals


inventory = get_inventory(INPUT_FILEPATH)
calorie_totals = get_calorie_totals(inventory)
most_calories = max(calorie_totals)

# inventory is splitting correctly
print('💚' if inventory[0] == [7769, 6798, 11685, 10826, 11807, 5786, 7932] else '❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌')

# calorie totals returns the correct sum of the first inventory in the test above
print('💚' if calorie_totals[0] == 62603 else '❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌')

# solution 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
print('⭐️' if most_calories == 71780 else '❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌') # first try 🙌