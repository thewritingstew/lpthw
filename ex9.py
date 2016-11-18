# create variables with strings, including new line characters (\n) in months
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints to screen the string and the values in the variables
print "Here are the days: ", days
print "Here are the months: ", months

# this three quote string allows for multiple lines to be printed, just as
# they are shown in the code...in other words, line breaks in the code
# are line breaks in the console output
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""