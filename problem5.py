#Exercise 5 (and Solution)
#http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
#Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#solution
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print "The following numbers appear in boths lists:"
print list(set(a).intersection(set(b)))
    
