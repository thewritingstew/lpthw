#============================================================
# beginning of original exercise
#============================================================

print "How old are you?",
age = raw_input() # accepts input with no prompt
print "How tall are you?",
height = raw_input('--> ') # accepts input with '--> ' prompt
print "How much do you weigh?",
weight = raw_input() # accepts input with no prompt

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#============================================================
# end of original exercise
#============================================================


#============================================================
# beginning of extra practice with raw_input()
#============================================================

## variable to store a check for valid entry
#is_valid = 0
#
## as long as is_valid is not true
#while not is_valid :
#    
#    # try the following
#    try :
#        
#        # set choice to the raw_input if it is an integer
#        choice = int ( raw_input('How old are you (enter integer): ') )
#        is_valid = 1 # set to 1 to validate input as integer
#
#    # if an integer isn't entered by the user, then there will be a
#    # "ValueError" when the code tries to interpret it. The following
#    # couple lines of code catches that exception and handles it
#    # by printing another line. Once this has happened, the while loop
#    # repeats, which means the user will be asked for their age again.
#    except ValueError, e :
#        print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
#
## this if...elif...else sequence takes the integer and prints a response
## based on the value of the integer
#if choice <= 12:
#    print ("You are a child...")
#elif choice <= 19:
#    print ("You are a teenager...")
#elif choice > 20:
#    print ("You are an adult...")
#else:
#    print ("You aren't a teenager or a full adult...")

#============================================================
# end of extra practice with raw_input()
#============================================================
