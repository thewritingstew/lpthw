# gets us ready to import args from the command line
from sys import argv

# the runtime arguments are stored in argv
script, input_file = argv

# function to print the entire file
def print_all(f):
    print f.read()

# function to go to the start of the file
def rewind(f):
    f.seek(0)

# function to print the line count and a single line of a file
def print_a_line(line_count, f):
    print line_count, f.readline()

# creates a file object with the input_file argument submitted at runtime
current_file = open(input_file)

print "First let's print the whole file:\n"
# calls the print_all function to print the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# calls the rewind function to go back to start of the file
rewind(current_file)

print "Let's print three lines:"
# Prints the number 1, and then the current line of the file. Note that this
# number 1 is not tied to the actual point in the file that is the first
# line, but our code above sets us up for this to match. If we actually
# wanted to know which line we are on, we'd have to do something a little
# more robust. 
current_line = 1
# sends the values of current_line and current_file to the print_a_line function
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
