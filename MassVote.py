def MassVote(N, Votes):
    all_votes = 0
    max_votes = max(Votes)
    for i in range(N):
        all_votes += Votes[i]
    if Votes.count(max_votes) > 1:
        return 'no winner'
    percent_win = round((max_votes / all_votes) * 100, 3)
    if percent_win > 50:
        return f'majority winner {Votes.index(max_votes) + 1}'
    else:
        return f'minority winner {Votes.index(max_votes) + 1}'
