my_name = 'Mathew A. Jones'
my_age = 31 # this is my actual age
my_height = 6.0 # inches
my_weight = 285 # lbs
my_eyes = 'Hazel'
my_teeth = 'White..ish'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually thats pretty heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d. %d. and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)