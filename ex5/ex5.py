name = 'Mathew A. Jones'
age = 31 # this is my actual age
height = 6.0 # inches
weight = 285 # lbs
eyes = 'Hazel'
teeth = 'White..ish'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats pretty heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d. %d. and %d I get %d." % (age, height, weight, age + height + weight)

# Convert pounds to kilo's
pounds = 280
kilos = pounds * 0.45359237
print "%r pounds equals %r kilos." % (pounds, kilos)
