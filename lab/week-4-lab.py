#!/usr/bin/env python3

# TODO: Assign a blank dictionary called ballot
ballot = {}
file = open(".inputs/.votes","r")
text = file.read()
#for V in text.split():
for V in text.split("\n"):
    try:
        ballot[V] += 1
    except:
        ballot[V] = 1
# TODO: Loop over file's contents
#       - incrementing candidates' vote count if already in dictionary
#       - adding candidate to the ballot if not already a key
# HINT: Can use a "try" or an "if" to do this.

winner = None
max_votes = 0
#print(ballot)
#W = ballot[G. Wiz]
for candidate in ballot:
    votes = ballot[candidate]
    #if ballot[candidate] >= W:
    #    winner = candidate              <-- this programs the _answer_, not the _solution_
    #    max_votes = ballot[candidate]
    print(f"{candidate} received {votes} votes.")
    if votes > max_votes:
        max_votes = votes
        winner = candidate
   
    
# TODO: Iterate over ballot dictionary to:
#       - list each candidate and total votes they received
#       - determine the winner of the election
#         - assign the name of the winner to winner, and
#           vote count to max_votes

print(f"The winner is {winner} -- with {max_votes} votes.")
