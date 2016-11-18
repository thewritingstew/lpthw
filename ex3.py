# prints the text in quotes
print "I will now count my chickens:"

# prints the string on one line, and then on the next 
# line prints the result of the math, with order of 
# operations being like 25 + ( 30 / 6) for the Hens, 
# and 100 - ( ( 25 * 3 ) % 4 ). On the latter, the % 
# is the modulo operation, so 75 mod 4 equals 3 because 
# the remainder when 75 is divided by 4 is 3. 
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

# displays the string to the screen
print "Now I will count the eggs:"

# does the math like so: 3 + 2 + 1 - 5 + ( 4 % 2 ) - ( 1 / 4 ) + 6
# which equals: 3 + 2 + 1 - 5 + (0) - (0) + 6
# which is 7. Interesting to note that 1/4 is 0, perhaps because 
# we are dealing with integers and a floor, rather than with 
# floating points. You only need to have one of the denominator 
# or numerator be a floating point to have a division work as 
# floating point. A floating point in any part of the math makes the 
# answer floating point, but won't make all parts of the equation 
# floating point. 

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 # original
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6 # floating point in division portion
print 3 + 2.0 + 1 - 5 + 4 % 2 - 1 / 4 + 6 # floating point in addition makes answer floating point, but 1/4 is still 0.

# displaying another string
print "Is it true that 3 + 2 < 5 - 7?" 

# returns true or false, based on a comparison of 3 + 2 and 5 - 7, 
# with the comparison being less than. Answers the question 
# "Is 3 + 2 less than 5 - 7?", and prints the answer.
print 3 + 2 < 5 - 7

# displays the string, and then the result of the math.
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

# displays the string
print "Oh, that's why it's False."

# displays the string
print "How about some more."

# displays the string and then the boolean for the comparison
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2