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

def parse_section_assignment(section_assignment):
    assignment_1, assignment_2 = section_assignment.split(',')
    return assignment_1.split('-') + assignment_2.split('-')

def increment_enclosed_count(section_assignment, count):
    assignment_1_start, assignment_1_end, assignment_2_start, assignment_2_end = parse_section_assignment(section_assignment)
    if (
            (int(assignment_1_start) <= int(assignment_2_start) and int(assignment_1_end) >= int(assignment_2_end)) or 
            (int(assignment_2_start) <= int(assignment_1_start) and int(assignment_2_end) >= int(assignment_1_end))
        ):
        count += 1
    return count

def increment_overlap_count(section_assignment, count):
    assignment_1_start, assignment_1_end, assignment_2_start, assignment_2_end = parse_section_assignment(section_assignment)
    if (
            (int(assignment_1_start) >= int(assignment_2_start) and int(assignment_1_start) <= int(assignment_2_end)) or
            (int(assignment_2_start) >= int(assignment_1_start) and int(assignment_2_start) <= int(assignment_1_end))
        ):
        count += 1
    return count

def get_enclosed_count(section_assignments):
     # An assignment that fully overlaps with another assignment
     # Example 1: '1-5 encloses 2-5'
     # Example 2: '2-5 encloses 1-5'
    return sum([increment_enclosed_count(section_assignment, 0) for section_assignment in section_assignments])

def get_overlap_count(section_assignments):
     # Any overlap between the two pairs
     # Example 1: 5-7,7-9 overlaps in a single section, 7
     # Example 2: 2-8,3-7 overlaps all of the sections 3 through 7
    return sum([increment_overlap_count(section_assignment, 0) for section_assignment in section_assignments])

# Code goes here
section_assignments = get_input()
enclosed_count = get_enclosed_count(section_assignments)
overlap_count = get_overlap_count(section_assignments)

# Stdout here
print('--')

# Tests
# solution 1: In how many assignment pairs does one range fully contain the other?
# attempt 1: 278, too low
run_star_test(enclosed_count, 542)
# solution 2: In how many assignment pairs do the ranges overlap?
run_star_test(overlap_count, 900)