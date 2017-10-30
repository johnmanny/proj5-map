#! /bin/bash
#
# Kill all current instances of flask_map on this machine
# (recycled from project 4)
#

# Grep for all running processes containing flask_map in description
# EXCEPT the grep command itself; turn them into 'kill' commands and
# execute the commands with bash
#
ps -x | grep flask_map | grep -v grep | \
    awk '{print "kill " $1}' | bash


