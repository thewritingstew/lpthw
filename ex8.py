# creates a variable for character formatters
formatter = "%r %r %r %r"

# a bunch of lines to print using the formatter variable
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

# printing the contents of formatter in each of the four slots in the initial 
# string that has four character formatters in it. 
print formatter % (formatter, formatter, formatter, formatter)

# multi-line coding to make sure the contents don't go beyond the 80 character
# wall. 
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)