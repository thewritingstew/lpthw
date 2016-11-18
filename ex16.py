# import argv method from sys module
from sys import argv

# store runtime args for use
script, filename = argv

# print warning about erasing file. Have them abort if they don't want to
# continue with the erasing of the file.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# prompt for their response.
raw_input("?")

# Opens the file in write mode...'target' file object created.
print "Opening the file..."
target = open(filename, 'w')

# truncates the file using the truncate() method. Note that this method does
# not have to be used if we are opening the file in write mode, since write
# mode erases all contents of the file.
print "Truncating the file. Goodbye!"
target.truncate()

# gathers three lines from the user
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# writes the lines to the file, with a new line between each one
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# closes the file
print "And finally, we close it."
target.close()