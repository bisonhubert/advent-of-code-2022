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

def get_start_of_packet_marker(signal, distinct_chars=4):
    substr = ''
    marker = None
    for indx, char in enumerate(signal):
        substr += char
        if len(substr) == distinct_chars:
            if is_marker(substr):
                marker = indx + 1
                break
            substr = substr[1:]
    return marker

# Code goes here
test_input_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test_input_2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test_input_3 = 'nppdvjthqldpwncqszvftbrmjlhg'
test_input_4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test_input_5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
test_marker_disctinct_4 = get_start_of_packet_marker(test_input_1)
test_marker_disctinct_14_1 = get_start_of_packet_marker(test_input_1, distinct_chars=14)
test_marker_disctinct_14_2 = get_start_of_packet_marker(test_input_2, distinct_chars=14)
test_marker_disctinct_14_3 = get_start_of_packet_marker(test_input_3, distinct_chars=14)
test_marker_disctinct_14_4 = get_start_of_packet_marker(test_input_4, distinct_chars=14)
test_marker_disctinct_14_5 = get_start_of_packet_marker(test_input_5, distinct_chars=14)

input = get_input()
marker_1 = get_start_of_packet_marker(input)
marker_2 = get_start_of_packet_marker(input, distinct_chars=14)

# Stdout here
print('--')

# Tests
# prompt examples
run_unit_test(test_marker_disctinct_4, 7)
run_unit_test(test_marker_disctinct_14_1, 19)
run_unit_test(test_marker_disctinct_14_2, 23)
run_unit_test(test_marker_disctinct_14_3, 23)
run_unit_test(test_marker_disctinct_14_4, 29)
run_unit_test(test_marker_disctinct_14_5, 26)

# solution 1: How many characters need to be processed before the first start-of-packet marker is detected?
run_star_test(marker_1, 1855)

# solution 2: How many characters need to be processed before the first start-of-message marker is detected?
run_star_test(marker_2, 3256)