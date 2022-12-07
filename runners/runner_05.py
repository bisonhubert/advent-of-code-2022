import itertools
from operator import itemgetter
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
            procedure.append({'crate_count': int(crate_count), 'move_from': int(move_from) - 1, 'move_to': int(move_to) - 1})
        if line == '\n':
            has_procedure_started = True
    return procedure

def get_stacks(supplies):
    stacks = list(map(list, itertools.zip_longest(*supplies, fillvalue=None)))
    return [
        list(filter(lambda x: x is not None, stack))
        for stack in stacks
    ]

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

def process_instruction(stacks, crate_count, move_from, move_to):
    crates_to_move = stacks[move_from][-crate_count:]
    crates_to_move.reverse()
    stacks[move_to] = stacks[move_to] + crates_to_move
    stacks[move_from] = stacks[move_from][:-crate_count]
    return stacks

def move_stacks(stacks, procedure):
    for instruction in procedure:
        crate_count, move_from, move_to = itemgetter('crate_count', 'move_from', 'move_to')(instruction)
        process_instruction(stacks, crate_count, move_from, move_to)
    return stacks

def get_top_crates(stacks):
    return [stack[-1] for stack in stacks if len(stack) > 0]

def get_top_crates_as_str(stacks):
    return ''.join(get_top_crates(stacks))

# Code sample from challenge
test_stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
test_stacks_copy = test_stacks.copy()
test_procedure = get_procedure(['\n', 'move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2'])
test_new_stacks = move_stacks(test_stacks_copy, test_procedure)
test_top_crates = get_top_crates_as_str(test_new_stacks)
run_unit_test(test_top_crates, 'CMZ')

# Code goes here
supplies, procedure = get_input()
stacks = get_stacks(supplies)
copied_stacks = stacks.copy()
new_stacks = move_stacks(copied_stacks, procedure)
top_crates = get_top_crates_as_str(new_stacks)

# Tests
# test get_input()
run_unit_test(len(supplies), 8)
run_unit_test(supplies, [
        ['F', 'R', 'C', 'F', 'L', 'Q', 'F', 'D', 'P'],
        ['D', 'S', 'R', 'V', 'T', 'C', 'C', 'N', 'G'],
        ['B', 'N', 'N', 'N', 'Q', 'W', 'L', 'Q', 'S'],
        ['Z', 'J', 'J', 'G', 'F', 'Z', 'S', 'M', None],
        ['T', 'H', 'G', 'R', None, 'B', 'N', 'T', None],
        ['J', None, 'Z', 'T', None, 'R', 'H', 'J', None],
        ['R', None, 'F', 'Q', None, 'G', 'M', None, None],
        ['N', None, 'Q', None, None, 'N', None, None, None]
    ]
)
run_unit_test(procedure[0], {'crate_count': 3, 'move_from': 8, 'move_to': 3})
run_unit_test(procedure[1], {'crate_count': 2, 'move_from': 4, 'move_to': 1})
run_unit_test(procedure[-1], {'crate_count': 3, 'move_from': 5, 'move_to': 8})

# test get_stacks()
run_unit_test(stacks, [
        ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'],
        ['R', 'S', 'N', 'J', 'H'],
        ['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q'],
        ['F', 'V', 'N', 'G', 'R', 'T', 'Q'],
        ['L', 'T', 'Q', 'F'],
        ['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N'],
        ['F', 'C', 'L', 'S', 'N', 'H', 'M'],
        ['D', 'N', 'Q', 'M', 'T', 'J'],
        ['P', 'G', 'S']
    ]
)

# after transposing the supplies into stacks
# run_unit_test(stacks[0], ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'])
# run_unit_test(supplies[1], ['R', 'S', 'N', 'J', 'H', None, None, None])
# run_unit_test(procedure[1], {'num_crates': 2, 'move_from': 5, 'move_to': 2})
# import pdb;pdb.set_trace()

# solution x: <prompt-from-website>
# attempt 1: NHQQFNMJS (ran against the wrong stack)
# attempt 2: FGFRZQMQS (pulling off the whole list of crates and placing it back on the other stack in the same order)
# attempt 3: LRFFGZQCT (pulling off the whole list of crates and placing it back on the other stack in reverse order)
run_star_test(top_crates, 'QNNTGTPFN')