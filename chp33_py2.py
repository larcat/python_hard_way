#i = 0
#numbers = []

def num_loop(max, increment):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottomm i is %d" % i

print "The numbers: "

num_loop(12, 3)
#for num in numbers:
#    print num