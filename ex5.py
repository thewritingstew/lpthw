name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# for changing inches to centimeters, cm = in * 2.54
cm_height = height * 2.54

# for changing pounds to kilograms, lb * 2.204 = kg
kg_weight = weight * 2.204

print "Let's talk about %s." % name
print "He's %d inches tall, which is %.2f cm tall." % (height, cm_height)
print "He's %d pounds heavy, which is %.2f kg." % (weight, kg_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)