

# Convert points (0,1,2,3) to scores (love, 15, 30, 40)
def point_to_score(score):

    if score == 0:
        return "love"
    elif score == 1:
        return "15"
    elif score == 2:
        return "30"
    elif score == 3:
        return "40"
    else:
        raise ValueError('Invalid score ' + score)


# Call the scores.
def call_the_scores(score1, score2):

    if score1 >= 4 and (score1-score2) >= 2:
        return "Match player one", True     # True - game finish
    elif score2 >= 4 and (score2-score1) >= 2:
        return "Match player two", True     # True - game finish
    elif score1 >= 3 and (score2 == score1):
        return "deuce", False
    elif score1 >= 4 and (score1-score2) == 1:
        return "advantage player one", False
    elif score2 >= 4 and (score2-score1) == 1:
        return "advantage player two", False
    elif score1 == score2:
        return point_to_score(score1) + "-" + "all", False
    else:
        return point_to_score(score1) + "-" + point_to_score(score2), False


def print_usage():
    print("Enter 0 to call the score, 1 if Player1 scores and 2 if Player2 scores:")


if __name__ == "__main__":
    print('Enter 0 to call the score, 1 if Player1 scores and 2 if Player2 scores:')

    # Initialise Player1 and Player2 to zero scores
    player1 = 0
    player2 = 0
    matchWon = False
    printScore = False

    # Read from stdin to decide who has score the next point.
    while True:
        printScore = False
        try:
            whoScores = int(raw_input())
            if whoScores == 1:
                player1 += 1
            elif whoScores == 2:
                player2 += 1
            elif whoScores == 0:
                printScore = True
            else:
                print "Invalid Input!"
                print_usage()
        except ValueError:      # Catch user entering string or other invalid input
            print "Invalid Input!"
            print_usage()

        message, matchWon = call_the_scores(player1, player2)

        # Print the score when the game finished
        if matchWon:
            print message
            print "Game finished."
            exit(0)
        elif printScore:
            # Print the score
            print message



