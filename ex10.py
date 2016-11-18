# a bunch of variables with different escapes
tabby_cat = "\tI'm tabbed in." # \t tabs this in
persian_cat = "I'm split\non a line." # \n means new line
backslash_cat = "I'm \\ a \\ cat." # \\ puts a backslash between words

# multi-line string
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# prints the strings to the screen
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# this code makes a little progress bar by printng each character in the
# []...the \r returns the cursor to the front of the line and then prints
# the next character on top of what was there already. On my computer, this
# goes way to fast to be useful. It would be good if it refreshed every half
# second at the fastest.
# code start ============

    #while True:
    #    for i in ["/", "-", "|", "\\", "|"]:
    #        print "%s\r" % i,

# code end ==============