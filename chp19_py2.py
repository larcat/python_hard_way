# Defines the cheese_and_crackers function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints some fluff and then the cheese_count var
    print "You and %d cheeses!" % cheese_count
    # Prints some fluff and then the boxes_of_crackers var
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Fluff
    print "Man that's enough for a party!"
    # Fluff
    print "Get a blanket.\n"

# Fluff
print "We can just give the function numbers directly:"
# c_&_C with 20 and 30 as count, boxex
cheese_and_crackers(20, 30)

# Fluff
print "OR, we can use variables from our script:"
# Sets var
amount_of_cheese = 10
# Sets var
amount_of_crackers = 50

# Calls func with preset vars above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Fluff
print "We can even do math inside too:"
# Calls func with mathy args
cheese_and_crackers(10 + 20, 5 + 6)

# Fluff
print "And we can combine the two, variables and math:"
# Calls func with mathy + vary args
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 1) Ok
# 2) No
# 3) Ok

def maths_lol(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)

maths_lol(1, 2, 3)

lol = 1
lolol = 2
lololol = 3

maths_lol(lol, lolol, lololol)

maths_lol(lol + lol, lolol + lolol, lololol + lololol)

maths_lol(lol + 1, lolol + 1, lololol + 1)


# Isn't 4 enough for you you bastard?
