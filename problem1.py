##problem 1
#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = raw_input ("What is your name?")
age = raw_input ("What is your current age?")
current_year = raw_input ("What is the current year?")
year_of_birth = int(current_year) - int(age)
year_of_100 = year_of_birth + 100
print"Hi " + name + " you will turn 100 years old in the year:"
print year_of_100