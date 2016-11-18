numbers = []
l_len = 6

def listLoader(nums):
    i = 0
    while i < nums:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

listLoader(l_len)

print "The numbers: "

for num in numbers:
    print num
