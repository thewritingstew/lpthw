numbers = []
l_len = 6
increment = 2

def listLoader(nums, increment):
    for i in range(0, nums, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

listLoader(l_len, increment)

print "The numbers: "

for num in numbers:
    print num
