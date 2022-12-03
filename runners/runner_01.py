from tests import run_star_test, run_unit_test

INPUT_FILEPATH = './inputs/input_01.py'

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

def get_inventory_details(inventory):
    inventory_details = []
    for indx, elf_inventory in enumerate(inventory):
        inventory_details.append(sum(elf_inventory))
    return inventory_details

def top_x_most_calories(inventory_details, elf_count=3):
    top_3_most_calories = 0
    inventory_details_copy = inventory_details[:]
    for i in list(range(elf_count)):
        max_calories = max(inventory_details_copy)
        top_3_most_calories += max_calories
        # print('top 3 most', top_3_most_calories)
        inventory_details_copy.remove(max_calories)
    return top_3_most_calories

inventory = get_inventory(INPUT_FILEPATH)
inventory_details = get_inventory_details(inventory)
most_calories = top_x_most_calories(inventory_details, elf_count=1)
top_3_most_calories = top_x_most_calories(inventory_details)

# Tests

# inventory is splitting correctly
# run_unit_test(inventory[0], [7769, 6798, 11685, 10826, 11807, 5786, 7932])
# calorie totals returns the correct sum of the first inventory in the test above
# run_unit_test(inventory_details[0], 62603)
# solution 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
run_star_test(most_calories, 71780) # first try 🙌
# solution 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
# attempt_1 = 215340, too high
run_star_test(top_3_most_calories, 212489)