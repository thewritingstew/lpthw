# import argv from the sys module so that we can take arguments at runtime
from sys import argv

# assigns the runtime arguments to variables script, user_name
script, user_name = argv
# sets up the prompt characters
prompt = '=> '

# prints some initial comments to the screen, including the runtime arguments
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# gathers input from the user and stores it in a variable named 'likes'
likes = raw_input(prompt)

# asks a question, displays a prompt and stores user input into variable 'lives'
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# asks a question, displays a prompt, stores user input into variable 'computer'
print "What kind of computer do you have?"
computer = raw_input(prompt)

# multi-line print with three formatted characters, which are populated with
# 'likes', 'lives', and 'computer'
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. 
And you have a %r computer. Nice. 
""" % (likes, lives, computer)