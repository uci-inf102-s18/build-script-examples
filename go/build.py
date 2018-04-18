#!/usr/bin/env python

import subprocess

# variables
executables = ["Main.go"]
compiler = 'go'

# build command
command = [compiler, "build"]
command.extend(executables)

# build program
subprocess.call(command)
