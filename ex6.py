# variable to hold a string
x = "There are %d types of people." % 10
# variable to hold a string
binary = "binary"
# variable to hold a string
do_not = "don't"
# variable to hold a string
y = "Those who know %s and those who %s." % (binary, do_not)

# displays variable
print x
# displays variable
print y

# displays string and variable
print "I said: %r." % x
# displays string and variable
print "I also said: '%s'." % y

# creates variable holding boolean value
hilarious = False
# variable to hold a string
joke_evaluation = "Isn't that joke so funny?! "

# displays a string that has format characters in it, and 
# tells it what the format character should be.
print joke_evaluation % hilarious

# variable to hold a string
w = "This is the left side of..."
# variable to hold a string
e = "a string with a right side."

# displays two strings, concatenated together.
print w + e