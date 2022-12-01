#/bin/bash

# CAUTION: THIS SCRIPT WILL OVERWRITE EXISTING FILES
# todobison Run a check and warn if you are going to overwrite a file.
# Otherwise you will need to rely on version control to revert overwrites.

cp templates/runner.py runner_$1.py
cp templates/input.py input_$1.py