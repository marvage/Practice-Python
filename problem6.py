#Exercise 6 (and Solution)

#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

#Exercise 6 (and Solution)

#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

#ask user to input a string
the_string = raw_input("Is your word or phrase a palindrome? Enter it here to find out:")

#strip out any spaces
the_string_stripped = the_string.replace(' ', '')

#reverse the order using the extended slicing syntax in python (info here: https://docs.python.org/2/whatsnew/2.3.html#extended-slices)
reverse_string = the_string_stripped[::-1]

#compare the strings and print the appropriate result

if the_string_stripped == reverse_string:
  print "Yeppers, ", the_string, " is a palindrome."
else:
  print "Nope, ", the_string, "ain't no palindrome."

