import os
import sys

from tests import run_star_test, run_unit_test

def get_input_filepath(filename):
    day = filename.split('/')[-1].split('_')[-1].split('.')[0]
    return f'./inputs/input_{day}.txt'

def parse_input(filepath):
    f = open(filepath)
    readlines = f.readlines()
    return readlines[0]

def get_input():
    current_filename = os.path.abspath(sys.argv[0])
    INPUT_FILEPATH = get_input_filepath(current_filename)
    return parse_input(INPUT_FILEPATH)

def is_marker(subset):
    return len(subset) == len(set(subset))

def get_start_of_packet_marker(signal):
    substr = ''
    marker = None
    for indx, char in enumerate(signal):
        substr += char
        if len(substr) == 4:
            if is_marker(substr):
                marker = indx + 1
                break
            substr = substr[1:]
        # import pdb;pdb.set_trace()
    return marker

# Code goes here
test_input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test_marker = get_start_of_packet_marker(test_input)

input = get_input()
marker = get_start_of_packet_marker(input)
print('marker', marker)



# Stdout here
print('--')

# Tests
# prompt example
run_unit_test(test_marker, 7)

# solution 1: How many characters need to be processed before the first start-of-packet marker is detected?
run_star_test(marker, 1855)