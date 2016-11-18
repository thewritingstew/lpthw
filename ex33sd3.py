numbers = []
l_len = 25
increment = 3

def listLoader(nums, increment):
    i = 0
    while i < nums:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

listLoader(l_len, increment)

print "The numbers: "

for num in numbers:
    print num
