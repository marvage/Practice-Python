# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

input = int(raw_input("Enter a random whole number greater than zero:"))
if input % 2 == 0:
    print "Your number is even!"
else:
    print "Your number is odd!"