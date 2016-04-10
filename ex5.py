in_to_cm = 2.54
lb_to_kg = 0.453592
name = 'Jesse D. Hagberg'
age = 37 # not a lie
height = 68 # inches
weight = 165 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "It sounds better stated as %d centimeters." % (in_to_cm * height)
print "He's %d pounds heavy." % weight
print "That's %d kilograms." % (lb_to_kg * weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age ,height ,weight ,age + height + weight)