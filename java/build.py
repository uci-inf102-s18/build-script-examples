#!/usr/bin/env python

import subprocess

# variables
executables = ['Main.java']
compiler = 'javac'

# build command
command = [compiler]
command.extend(executables)

# build program
subprocess.call(command)
