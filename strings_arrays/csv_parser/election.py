import operator


def  electionWinner(votes):
    vote_count = {}
    
    for candidate in votes:
        # print candidate
        vote_count[candidate] = vote_count.get(candidate, 0) + 1
    print vote_count
    winner = max(vote_count.iteritems(), key=operator.itemgetter(0))[0]
    print winner
    return winner


electionWinner(['alex', 'michael', 'michael', 'mary', 'mary', 'victor', 'victor', 'x', 'x'])