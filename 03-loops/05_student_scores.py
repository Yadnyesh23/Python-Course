# You’re building a simple student report generator that combines names and scores.

# Tasks:

# Define two lists -  one with student names and one with their scores.

# Use the zip() function to pair each student with their score.

# Return a list of strings in the format "Name scored X marks"

names = ["abc", "def", "ghi"]
marks = [100, 30, 50]

for name , mark in zip(names, marks):
    print(f"{name} got marks {mark}")