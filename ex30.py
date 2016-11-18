people = 30
cars = 40
trucks = 15

# checks to see if there are more cars than people
if cars > people:
    # if there are more cars, it prints this
    print "We should take the cars."
# otherwise it checks to see if there are less cars than people
elif cars < people:
    # and if so it prints this
    print "We should not take the cars."
# if none of the other conditions are met, it prints this
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
