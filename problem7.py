#Exercise 7 (and Solution)
From http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#even_numbers = []
#
#for x in a:
#  if x % 2 == 0:
#    even_numbers.append(x)
#print even_numbers

#to condense this using a list comprehension approach...
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers = [x for x in list if x %2 == 0]
print even_numbers
