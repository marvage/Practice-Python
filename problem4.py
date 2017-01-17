#Exercise 4 from http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

x = int(raw_input("Enter a number:"))
y = range (1, x)
divisor_list = []

for i in (y):
 if x % i == 0:
   divisor_list.append(i)
print "A List of the divisors of:", x
print divisor_list