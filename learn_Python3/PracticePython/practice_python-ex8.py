""""
Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message
of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
plays = ["rock", "paper", "cisor"]
player1 = input("Please enter one of the following: %s :" % plays)
#rem_plays = plays.remove("%s" % player1)
#print(rem_plays)

player2 = input("Player 2 please enter one of the following: %s " % plays)

#print("Player one and 2 selected %s and %s respectively." % (player1, player2))
print(player1)
print(player2)

if player1 == player2:
    print("You both selected the same option. Please Start over.")
    exit(code=255)
elif:
    player1 == plays[0] and player2 == plays[1]
    print(plays[1] + " wins!")
elif:
    player1 == plays[0] and player2 == plays[2]
    print(player1 + " wins!")
elif:
    player1 == plays[0] and player2 == plays[2]
    print(player1 + " wins!")