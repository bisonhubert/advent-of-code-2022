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

def get_overlap_count(section_assignments):
     # Any overlap between the two pairs
     # Example 1: 5-7,7-9 overlaps in a single section, 7
     # Example 2: 2-8,3-7 overlaps all of the sections 3 through 7
    overlap_count = 0
    for section_assignment in section_assignments:
        assignment_1, assignment_2 = section_assignment.split(',')
        assignment_1_start, assignment_1_end = assignment_1.split('-')
        assignment_2_start, assignment_2_end = assignment_2.split('-')
        # print('assignment_1', assignment_1)
        # print('assignment_2', assignment_2)
        if (
                (int(assignment_1_start) >= int(assignment_2_start) and int(assignment_1_start) <= int(assignment_2_end)) or
                (int(assignment_2_start) >= int(assignment_1_start) and int(assignment_2_start) <= int(assignment_1_end))
            ):
            # import pdb;pdb.set_trace()
            overlap_count += 1
    return overlap_count

# Code goes here
section_assignments = get_input()
enclosed_count = get_enclosed_count(section_assignments)
overlap_count = get_overlap_count(section_assignments)

# Stdout here
print('--')
print('overlap_count', overlap_count)

# Tests
# describe unit test
# run_unit_test(enclosed_count, 542)
# solution 1: In how many assignment pairs does one range fully contain the other?
# attempt 1: 278, too low
run_star_test(enclosed_count, 542)
# solution 2: In how many assignment pairs do the ranges overlap?
run_star_test(overlap_count, 900)