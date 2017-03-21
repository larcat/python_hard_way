#Prints
print "Mary had a little lamb."
#Prints with an inserted value
print "Its fleece was white as %s." % 'snow'
#Prints
print "And everywhere that Mary went."
#Prints "." 10 times in a row on the same line.
print "." * 10 # what'd that do? -- String multiplication is like R

#Let's assign some text to variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# And then print them out together in clever ways
# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 +end6, 
print end7 + end8 +end9 + end10 + end11 + end12
# Comma makes explicit continue on same line, at least for print
# Dunno if it works for other stuff
# Lets find out
# Prints the result of 2 plus 2 (it is 4)
print 2 + 2
#Prints "a", but keeps the printing on the same line because comma
print "a", 
#And here's the four after our a on the same line
print 2 + 2
# So it works for the line over all, but you cannot interrupt an expression
# and have it work right... i.e it doesn work with the comma after the plus
