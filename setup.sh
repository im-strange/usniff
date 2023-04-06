#!/bin/bash

custom_command="alias usniff='python usniff.py'"
echo "$custom_command" >> ~/.bashrc
source  ~/.bashrc
echo "SUCCESS"
