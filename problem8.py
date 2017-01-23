#Rock Paper Scissors      
#Exercise 8, from http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and #ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

while True:
    p1 = raw_input("Player 1: Rock, paper, or scissors?")
    p2 = raw_input("Play 2: Rock, paper, or scissors?")
    if p1 == p2:
        print ("Draw!")
    elif p1 == "rock" and p2 == "scissors":
        print ("Player 1 wins!")
    elif p1 == "scissors" and p2 == "paper":
        print ("Player 1 wins!")
    elif p1 == "paper" and p2 == "rock":
        print ("Player 1 wins!")
    elif p2 == "rock" and p1 == "scissors":
        print ("Player 2 wins!")
    elif p2 =="scissors" and p1 == "paper":
        print ("Player 2 wins!")
    elif p2 == "paper" and p1 == "rock":
        print ("Player 2 wins!")
    
    goAgain = raw_input ("Would you like to play again (Y or N)?").upper()
    if goAgain =="N":
        break

  