#!/usr/bin/env python

import subprocess
import os

# Variables
exe = 'Main'
interpreter = ''
text_file = 'pride-and-prejudice.txt'
solution_file = 'pride-and-prejudice-solution.txt'

# Get file path in os independent way
working_dir = os.getcwd()
test_files_location = os.path.join(working_dir, os.pardir)

text_loc = os.path.join(test_files_location, text_file)
solution_loc = os.path.join(test_files_location, solution_file)

# Run program
output = None
print('-------{}----------'.format(exe))

if interpreter == '':
	file_path = os.path.join(working_dir, exe)
	output = subprocess.check_output([file_path, text_loc]).splitlines()
else:
	file_path = exe
	output = subprocess.check_output([interpreter, file_path, text_loc]).splitlines()

solution = ""
with open (solution_loc, "r") as f:
	solution = f.read().splitlines()

# Test output on (1) number of words outputted, (2) correctness
passing = True
number_of_lines = 0
for out, sol in zip(output, solution):
	number_of_lines += 1
	
	if out == sol:
		continue
	else:
		print "Expected: {}, \tActually: {}".format(sol, out)
		passing = False

if passing and number_of_lines == 25:
	print "Passed!"
else:
	print "Failed..."
