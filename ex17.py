from sys import argv
from os.path import exists

script, from_file, to_file = argv

# commenting out next line to simplify the process
# print "Copying from %s to %s" % (from_file, to_file)

# this goes from opening the file to reading the file, all on one line.
#
#       indata = open(from_file).read()
#
# we can bypass the in_file part because we don't need it at this point, but
# this would cause problems when it is time to close the file (at least if
# we did it this way). There may be a way to do it where we can open the file
# and read it one one line, while still being able to create the file object
# in a way that allows us to close it later. Reading further on this topic, if
# we get to indata as shown above, the file object is closed automatically
# once that line runs. So it opens the file, reads it, and then closes it.

# creates input file object and data
in_file = open(from_file)
indata = in_file.read();

# commenting out next line to simplify the process
# print "The input file is %d bytes long" % len(indata)

# commenting out next line to simplify the process
# print "Does the output file exist? %r" % exists(to_file)
# commenting out next line to simplify the process
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# commenting out next line to simplify the process
# raw_input()

# writes the contents of indata to the out_file
out_file = open(to_file, 'w')
out_file.write(indata)

# lets the user know the script has completed and closes the file objects
print "Alright, all done."
out_file.close()
in_file.close()



