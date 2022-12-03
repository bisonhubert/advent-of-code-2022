import os
import sys

from tests import run_star_test, run_unit_test

def get_input_filepath(filename):
    day = filename.split('/')[-1].split('_')[-1].split('.')[0]
    return f'./inputs/input_{day}.txt'

def parse_input(filepath):
    # ['PcPlnShm\n'] ->  ['PcPlnShm']
    f = open(filepath)
    readlines = f.readlines()
    return [readline.strip() for readline in readlines]

def get_input():
    current_filename = os.path.abspath(sys.argv[0])
    INPUT_FILEPATH = get_input_filepath(current_filename)
    return parse_input(INPUT_FILEPATH)

def get_priority_map(letters):
    priority = 1
    priority_map = {}
    letters = [letter for letter in letters] + [letter.upper() for letter in letters]
    for letter in letters:
        priority_map[letter] = priority
        priority += 1
    return priority_map

# a - z :: 1 - 26
# A - Z :: 27 - 52
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PRIORITY_MAP = get_priority_map(LETTERS)


# PRIORITY_MAP = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8,
#     'i': 9,
#     'j': 10,
#     'k': 11,
#     'l': 12,
#     'm': 13,
#     'n': 14,
#     'o': 15,
#     'p': 16,
#     'q': 17,
#     'r': 18,
#     's': 19,
#     't': 20,
#     'u': 21,
#     'v': 22,
#     'w': 23,
#     'x': 24,
#     'y': 25,
#     'z': 26,
# }

rucksacks = get_input()
solution_1 = 0
solution_2 = 0
elf_group = []
for indx, rucksack in enumerate(rucksacks):
    elf_group.append(rucksack)
    if len(rucksack) % 2 != 0:
        print('broken, rucksack is not even')
    if (indx + 1) % 3 == 0:
        shared_items = [item for item in elf_group[0] if item in elf_group[1]]
        shared_item = [item for item in shared_items if item in elf_group[2]][0]
        solution_2 += PRIORITY_MAP[shared_item]
        elf_group = []
    compartment_1 = rucksack[:int(len(rucksack) / 2)]
    compartment_2 = rucksack[int(len(rucksack) / 2):]
    # run_unit_test(len(compartment_1), len(compartment_2))
    # run_unit_test(rucksack, compartment_1 + compartment_2)

    separated_items = [item for item in compartment_1 if item in compartment_2][0]
    solution_1 += PRIORITY_MAP[separated_items]
    

# Stdout here
print('--')

# Tests
# solution 1: Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
run_star_test(solution_1, 7831)
# solution 2: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
run_star_test(solution_2, 2683)