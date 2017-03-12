# Assigned and uses the formatter to finish the string with 10
x = "There are %d types of people." % 10
# String var
binary = "binary"
#Another string var
do_not = "don't"
#Assignes above string vars in the sring
y = "Those who know %s and those who %s." % (binary, do_not)

#Prints above assigned vars
print x
print y

#Uses the assigned string with a var in another string with a formatter
print "I said: %r." % x
#Uses the assigned string with a var in another string with a formatter
print "I also said: '%s'." % y

#Assigns boolean
hilarious = False
#Which is used cleverly here in assignment, converting the boolean to string
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints the cleverness
print joke_evaluation % hilarious

#Assigns strings
w = "This is the left side of..."
e = "a string with a right side."

#Uses math-seeming syntax to construct a string. Wy different than how you would use c()
print w + e
