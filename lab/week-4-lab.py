#!/usr/bin/env python3

# TODO: Assign a blank dictionary called ballot

file = # TODO: Open file at path .inputs/.votes

# TODO: Loop over file's contents
#       - incrementing candidates' vote count if already in dictionary
#       - adding candidate to the ballot if not already a key
# HINT: Can use a "try" or an "if" to do this.

winner = None
max_votes = 0

# TODO: Iterate over ballot dictionary to:
#       - list each candidate and total votes they received
#       - determine the winner of the election
#         - assign the name of the winner to winner, and
#           vote count to max_votes

print(f"The winner is {winner} -- with {max_votes} votes.")