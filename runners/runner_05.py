import os
import sys

from tests import run_star_test, run_unit_test

def get_input_filepath(filename):
    day = filename.split('/')[-1].split('_')[-1].split('.')[0]
    return f'./inputs/input_{day}.txt'

def parse_input(filepath):
    # i/o
    f = open(filepath)
    readlines = f.readlines()
    # parse input
    return readlines

def get_input():
    current_filename = os.path.abspath(sys.argv[0])
    INPUT_FILEPATH = get_input_filepath(current_filename)
    return parse_input(INPUT_FILEPATH)

# Code goes here
input = get_input()

# Stdout here
print('--')
print('input', input)

# Tests
# describe unit test
run_unit_test(1, 0)
# solution x: <prompt-from-website>
run_star_test(1, 0)