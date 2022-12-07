import itertools
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
    procedure = []
    has_procedure_started = False
    for line in readlines:
        if has_procedure_started:
            crate_count, move_from, move_to = line.strip().replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split(' ')
            procedure.append({'crate_count': int(crate_count), 'move_from': int(move_from), 'move_to': int(move_to)})
        if line == '\n':
            has_procedure_started = True
    return procedure

def get_stacks(supplies):
    return list(map(list, itertools.zip_longest(*supplies, fillvalue=None)))

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
stacks = get_stacks(supplies)

# Stdout here
print('--')

# Tests
# test get_input()
run_unit_test(len(supplies), 8)
run_unit_test(supplies, [['F', 'R', 'C', 'F', 'L', 'Q', 'F', 'D', 'P'],['D', 'S', 'R', 'V', 'T', 'C', 'C', 'N', 'G'],['B', 'N', 'N', 'N', 'Q', 'W', 'L', 'Q', 'S'],['Z', 'J', 'J', 'G', 'F', 'Z', 'S', 'M', None],['T', 'H', 'G', 'R', None, 'B', 'N', 'T', None],['J', None, 'Z', 'T', None, 'R', 'H', 'J', None],['R', None, 'F', 'Q', None, 'G', 'M', None, None],['N', None, 'Q', None, None, 'N', None, None, None]])
run_unit_test(procedure[0], {'crate_count': 3, 'move_from': 9, 'move_to': 4})
run_unit_test(procedure[1], {'crate_count': 2, 'move_from': 5, 'move_to': 2})
run_unit_test(procedure[-1], {'crate_count': 3, 'move_from': 6, 'move_to': 9})

# test get_stacks()
run_unit_test(stacks, [['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'],['R', 'S', 'N', 'J', 'H', None, None, None],['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q'],['F', 'V', 'N', 'G', 'R', 'T', 'Q', None],['L', 'T', 'Q', 'F', None, None, None, None],['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N'],['F', 'C', 'L', 'S', 'N', 'H', 'M', None],['D', 'N', 'Q', 'M', 'T', 'J', None, None],['P', 'G', 'S', None, None, None, None, None]])

# after transposing the supplies into stacks
# run_unit_test(stacks[0], ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'])
# run_unit_test(supplies[1], ['R', 'S', 'N', 'J', 'H', None, None, None])
# run_unit_test(procedure[1], {'num_crates': 2, 'move_from': 5, 'move_to': 2})
# import pdb;pdb.set_trace()

# solution x: <prompt-from-website>
# run_star_test(1, 0)