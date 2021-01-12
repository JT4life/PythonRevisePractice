def surf_winner(surfers):
    """
    After the competition, each surfer has a set of 3 performance scores:
    Style, Execution, and Difficulty.

    The style score is for the personality that is shown in the surfing performance. The Flare
    score is for the execution of the surf, including wave choice, speed, etc. The Difficulty score is
    for the difficulty of skills performed.

    The overall winner of the competition is the surfer with the highest score of the combined amounts.

    Example: Given these surfers and scores, 'Surfer_2' would be returned as the winner.
    surfers = {
              "Surfer_1": {
                  "style":1,
                  "execution": 2,
                  "difficulty":3
                  },
              "Surfer_2": {
                  "style":3,
                  "execution": 4,
                  "difficulty":0
                  },
              "Surfer_3":{
                  "style":0,
                  "execution": 0,
                  "difficulty":0
                  },
    }

    :param surfers: A dictionary of dictionaries of surfers and their scores
    :return: The name of the winner
    """

    winner = ''
    high_score = 0
    for surfer, scores in surfers.items():
        surfer_score = 0
        for style, point in scores.items():
            surfer_score += point
        if surfer_score > high_score:
            high_score = surfer_score
            winner = surfer
    return winner

surfers = {
            "Jane": {
                "style":10,
                "execution": 20,
                "difficulty":80
                },
            "Tyler": {
                "style":80,
                "execution": 2,
                "difficulty":56
                },
            "Stella":{
                "style":90,
                "execution": 10,
                "difficulty":74
                },
            "Jose":{
                "style":70,
                "execution": 80,
                "difficulty":45
                }
        }

a = surf_winner(surfers)
print(a)