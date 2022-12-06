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

# Code goes here
stacks, procedure = get_input()
import pdb;pdb.set_trace()

# Stdout here
# print('--')
# print('stacks', stacks)
# print('procedure', procedure)

# Tests
# describe unit test
output_1 = format_stacks(stacks[0])
import pdb;pdb.set_trace()
run_unit_test(output_1, 'N*Q**N***')
# run_unit_test(top_crates_test_output, 'NHQQFNMJS')
# solution x: <prompt-from-website>
# run_star_test(1, 0)