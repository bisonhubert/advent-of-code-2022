import os
import sys

from tests import run_star_test, run_unit_test

def get_input_filepath(filename):
    day = filename.split('/')[-1].split('_')[-1].split('.')[0]
    return f'./inputs/input_{day}.txt'

def get_supplies(readlines):
    supplies = []
    supply_rows = []
    for row in readlines:
        if row == '\n':
            break
        supply_rows.append(row)
    supply_rows = supply_rows[:-1]
    supply_rows.reverse()
    for indx, row in enumerate(supply_rows):
        supply_row = [crate.strip().replace('[', '').replace(']', '') for crate in row.split(' ')]
        if len(supply_row) == 9:
            supplies.append(supply_row)
        else:
            while '' in supply_row:
                first_space = supply_row.index('')
                remaining_spaces = supply_row[first_space:][:-1]
                supply_row = supply_row[:first_space]
                if len(set(remaining_spaces)) == 1:
                    num_remaining_spaces = len(remaining_spaces) // 3 or 1
                    supply_row = supply_row + [None for i in list(range(num_remaining_spaces))]
                else:
                    remaining_spaces = remaining_spaces[1:]
                    if '' in remaining_spaces:
                        supply_row.append(None)
                        remaining_spaces = remaining_spaces[3:]
                        supply_row += remaining_spaces
            if len(supply_row) != 9:
                missing_crates = 9 - len(supply_row)
                supply_row = supply_row + [None for i in list(range(missing_crates))]
            supplies.append(supply_row)
    return supplies

def get_procedure(readlines):
    return [None]

def parse_input(filepath):
    f = open(filepath)
    readlines = f.readlines()
    supplies = get_supplies(readlines)
    procedure = get_procedure(readlines)
    return supplies, procedure

def get_input():
    current_filename = os.path.abspath(sys.argv[0])
    INPUT_FILEPATH = get_input_filepath(current_filename)
    return parse_input(INPUT_FILEPATH)

# Code goes here
supplies, procedure = get_input()
# stacks = get_stacks(supplies)

# Stdout here
print('--')

# Tests
# test get_input()
run_unit_test(len(supplies), 8)
run_unit_test(supplies[0], ['F', 'R', 'C', 'F', 'L', 'Q', 'F', 'D', 'P'])
run_unit_test(supplies[1], ['D', 'S', 'R', 'V', 'T', 'C', 'C', 'N', 'G'])
run_unit_test(supplies[2], ['B', 'N', 'N', 'N', 'Q', 'W', 'L', 'Q', 'S'])
run_unit_test(supplies[3], ['Z', 'J', 'J', 'G', 'F', 'Z', 'S', 'M', None])
run_unit_test(supplies[4], ['T', 'H', 'G', 'R', None, 'B', 'N', 'T', None])
run_unit_test(supplies[5], ['J', None, 'Z', 'T', None, 'R', 'H', 'J', None])
run_unit_test(supplies[6], ['R', None, 'F', 'Q', None, 'G', 'M', None, None])
run_unit_test(supplies[7], ['N', None, 'Q', None, None, 'N', None, None, None])
# run_unit_test(procedure[0], {'num_crates': 3, 'move_from': 9, 'move_to': 4})
# after transposing the supplies into stacks
# run_unit_test(stacks[0], ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'])
# run_unit_test(supplies[1], ['R', 'S', 'N', 'J', 'H', None, None, None])
# run_unit_test(procedure[1], {'num_crates': 2, 'move_from': 5, 'move_to': 2})
# import pdb;pdb.set_trace()

# solution x: <prompt-from-website>
# run_star_test(1, 0)