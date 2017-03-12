name = 'Zed A. Shaw.'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches_to_cm = 2.45
lb_to_kg = .454

print ("Let's talk about %s." % name)
print ("He's %d inches tall." % height)
print ("He's %.2f cm tall" % round((height * inches_to_cm), 2)) # google yo
print ("He's %d pounds heavy." % weight)
print ("He's %.2f kg heavy." % round((height * lb_to_kg), 2))
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

#1
	