'''Given the participants' score sheet for your University '
Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up. '''



def secondScore(scores):
    high = max(scores)
    scores.sort(reverse=True)
    for i in scores:
        # print(i)
        if i < high:
            print(i)
            break

scores = [2, 3, 6, 6, 5]
secondScore(scores)