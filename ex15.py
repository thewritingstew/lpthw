# imports the argv method from the sys module
from sys import argv

# stores the runtime agruments as 'script' and 'filename'
script, filename = argv

# stores a file object as txt
txt = open(filename)

# prints the filename
print "Here's your file %r:" % filename
# prints the result of reading the file 'txt'
print txt.read()

# using raw_input to prompt the user to type the filename
print "Type the filename again:"
file_again = raw_input("> ")

# creates another file object, this time named txt_again
txt_again = open(file_again)

# prints the result of reading 'txt_again'
print txt_again.read()