from itertools import groupby

import os
import sys

from tests import run_star_test, run_unit_test

def get_input_filepath(filename):
    day = filename.split('/')[-1].split('_')[-1].split('.')[0]
    return f'./inputs/input_{day}.txt'

def format_stacks(stack):
    formatted_stack = ''
    crate_top = 0
    for i in list(range(len(stack))):
        if (i + 1) % 4 == 0:
            crate = stack[crate_top:i+1]
            if '[' in crate and ']' in crate:
                formatted_stack += crate.replace('[', '').replace(']', '').replace(' ', '')
                crate_top += i + 1
            else:
                formatted_stack += '*'
            print('crate', crate)
            print('formatted_stack', formatted_stack)
    print('hi')
    return formatted_stack

def mock_input():
    return [
        'N*Q**N***',
        'R*FQ*GM**',
        'J*ZT*RHJ*',
        'THGR*BNT*',
        'ZJJGFZSM*',
        'BNNNQWLQS',
        'DSRVTCCNG',
        'FRCFLQFDP'
    ]

def parse_input(filepath):
    f = open(filepath)
    readlines = f.readlines()
    stacks = readlines[:readlines.index('\n')]
    # stacks = format_stacks(readlines[:readlines.index('\n')])
    procedure = [readline.strip() for readline in readlines[readlines.index('\n')+1:]]
    return stacks, procedure

def get_input():
    current_filename = os.path.abspath(sys.argv[0])
    INPUT_FILEPATH = get_input_filepath(current_filename)
    return parse_input(INPUT_FILEPATH)

def get_top_crates(crates):
    top_crates = ['*' for i in list(range(len(crates)))]
    for indx, crate in enumerate(crates):
        top_crates[indx] = list(filter(lambda x: x != '*', crate))[0]
    return top_crates

def run(stacks, procedure):
    # move 3 from 9 to 4
    # ie: get 3 from stack 9
    # ie: move on top of stack 4
    for instruction in procedure:
        num_crates_to_move, move_from, move_to = instruction.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        instruction = {'num_crates_to_move': int(num_crates_to_move), 'move_from': int(move_from), 'move_to': int(move_to)}
        
        move_to = instruction.get('move_to')
        move_from = instruction.get('move_from')
        num_crates_to_move = instruction.get('num_crates_to_move')
        # import pdb;pdb.set_trace()
        slice_from = 9 - num_crates_to_move
        empty_spaces = '*'
        import pdb;pdb.set_trace()
        stacks[move_to][:slice_from] = stacks[move_from][:slice_from]
        for i in list(range(9)):
            if i >= slice_from:
                stacks[move_from][i] = '*'
        import pdb;pdb.set_trace()
    import pdb;pdb.set_trace()


# Code goes here
stacks, procedure = get_input()
mock_input = mock_input()

from itertools import zip_longest
list_of_lists = mock_input
tranposed_tuples = zip_longest(*list_of_lists, fillvalue=None)
transposed_tuples_list = list(tranposed_tuples)
# import pdb;pdb.set_trace()
top_crates = get_top_crates(transposed_tuples_list)
top_crates_after_procedure = run(transposed_tuples_list, procedure)

# Stdout here
# print('--')
# print('stacks', stacks)
# print('procedure', procedure)

# Tests
# test mock crates
run_unit_test(len(mock_input[0]), 9)
run_unit_test(len(mock_input[1]), 9)
run_unit_test(len(mock_input[2]), 9)
run_unit_test(len(mock_input[3]), 9)
run_unit_test(len(mock_input[4]), 9)
run_unit_test(len(mock_input[5]), 9)
run_unit_test(len(mock_input[6]), 9)
run_unit_test(len(mock_input[7]), 9)
run_unit_test(mock_input[0], 'N*Q**N***')
run_unit_test(mock_input[1], 'R*FQ*GM**')
run_unit_test(mock_input[2], 'J*ZT*RHJ*')
run_unit_test(mock_input[3], 'THGR*BNT*')
run_unit_test(mock_input[4], 'ZJJGFZSM*')
run_unit_test(mock_input[5], 'BNNNQWLQS')
run_unit_test(mock_input[6], 'DSRVTCCNG')
run_unit_test(mock_input[7], 'FRCFLQFDP')

# test top crates
run_unit_test(''.join(top_crates), 'NHQQFNMJS')

# run_unit_test(top_crates_test_output, 'NHQQFNMJS')
# solution x: <prompt-from-website>
# run_star_test(1, 0)