#!/usr/bin/env python

import subprocess

# variables
executables = ["Main.rs"]
compiler = 'rustc'
output = 'Main'

# build command
command = [compiler]
command.extend(executables)
command.extend(['-o', output])

# build program
subprocess.call(command)
