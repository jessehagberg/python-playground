#Exercise 21: Functions can Return Something
def add (a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, add(multiply(weight, divide(iq, 2)),100)))
print "That becomes: ", what, "Can you do it by hand?"

print "Here's my version of the simple math problem 5 * 4 + 9 / 3 * 2"
print" or otherwise shown as (5 * 4) + ((9 / 3) * 2)"

print "equals: %d" % add(multiply(5, 4), multiply(divide(9, 3), 2) )