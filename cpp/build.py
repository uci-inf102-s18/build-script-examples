#!/usr/bin/env python

import subprocess

# variables
executables = ['Main.cpp']
output_name = 'Main'
compiler = 'g++'
flags  = ['-std=c++11', '-o{}'.format(output_name)]

# build command
command = [compiler]
command.extend(flags)
command.extend(executables)

# build program
subprocess.call(command)
