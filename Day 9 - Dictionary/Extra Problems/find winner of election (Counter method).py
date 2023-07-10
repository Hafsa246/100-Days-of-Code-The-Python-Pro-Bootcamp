# find winner of election (Counter method)

from collections import Counter

def election_winner(input):
    votes = Counter(input)
    highest_vote = 0
    name = ""

    for vote in votes:
        if votes[vote] > highest_vote:
            highest_vote = votes[vote]
            name = vote
    
    return name


input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']

print(election_winner(input))