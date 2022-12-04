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
    return [readline.strip() for readline in readlines]

def get_input():
    current_filename = os.path.abspath(sys.argv[0])
    INPUT_FILEPATH = get_input_filepath(current_filename)
    return parse_input(INPUT_FILEPATH)

def get_enclosed_count(section_assignments):
     # An assignment that fully overlaps with another assignment
     # Example 1: '1-5 encloses 2-5'
     # Example 2: '2-5 encloses 1-5'
    enclosed_count = 0
    for section_assignment in section_assignments:
        assignment_1, assignment_2 = section_assignment.split(',')
        assignment_1_start, assignment_1_end = assignment_1.split('-')
        assignment_2_start, assignment_2_end = assignment_2.split('-')
        if (
                (int(assignment_1_start) <= int(assignment_2_start) and int(assignment_1_end) >= int(assignment_2_end)) or 
                (int(assignment_2_start) <= int(assignment_1_start) and int(assignment_2_end) >= int(assignment_1_end))
            ):
            enclosed_count += 1
    return enclosed_count

# Code goes here
section_assignments = get_input()
enclosed_count = get_enclosed_count(section_assignments)

# Stdout here
print('--')
print('enclosed_count', enclosed_count)

# Tests
# describe unit test
# run_unit_test(enclosed_count, 542)
# solution 1: In how many assignment pairs does one range fully contain the other?
# attempt 1: 278, too low
run_star_test(enclosed_count, 542)