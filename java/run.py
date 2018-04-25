#!/usr/bin/env python

import subprocess
import os

# Variables
executable = 'Main'
interpreter = 'java'
## Add class path
classpath_flag = ['-classpath', '.']
## Default value should be 1024k, increase the value below to your needed value.
stacksize_flag = '1024k'
text_file = 'pride-and-prejudice.txt'
solution_file = 'pride-and-prejudice-solution.txt'

# Get file path in os independent way
working_dir = os.getcwd()
test_files_location = os.path.join(working_dir, os.pardir)

text_location = os.path.join(test_files_location, text_file)
solution_loc = os.path.join(test_files_location, solution_file)

# Setup command
cmd = [interpreter]
## check if flags were defined and if so add them.
try:
	cmd.extend(classpath_flag)
	cmd.append('-Xss{}'.format(stacksize_flag))
except NameError:
	print("One or more flags were not defined, but continue...")
	pass

cmd.append(executable)
cmd.append(text_location)

# Run program
output = None
print('-------{}----------'.format(executable))

output = subprocess.check_output([interpreter,  executable, text_location]).splitlines()

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
