#My Solution to Problem 9 from http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the #number, then tell them whether they guessed too low, too high, or exactly right. (Hint: #remember to use the user input lessons from the very first exercise)

#I am assuming numpy is already installed

import random
GeneratedNumber = random.randint(1, 9)

while True:
    UserNumber = raw_input ("Enter a digit between 1 and 9 or 'exit' to leave:")
    if UserNumber == "exit":
      break
    elif int(UserNumber) == GeneratedNumber:
      print ("You guessed correctly!")
      break
    elif int(UserNumber) > GeneratedNumber:
      print ("Your guess is too high!")
    elif int(UserNumber) < GeneratedNumber:
      print ("your guess is too low!")
