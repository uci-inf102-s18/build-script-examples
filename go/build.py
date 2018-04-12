#!/usr/bin/env python

import subprocess

# variables
executables = ["main.go"]
compiler = 'go'

# build command
command = [compiler, "build"]
command.extend(executables)

# build program
subprocess.call(command)
