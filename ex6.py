# insert the literal '10' inside a string and store in variable x.
x = "There are %d types of people." % 10
# store the string "binary" into variable binary.
binary = "binary"
# store the string "don't" in variable do_not.
do_not = "don't"
# insert strings referenced by variables binary and do_not into another string and store the whole thing in variable y.
y = "Those who know %s and those who %s." % (binary, do_not)

#print the string referenced by variable x.
print x
#print the string referenced by variable y.
print y

# I'm not sure what repr() does yet but this conversion type converts the object stored in x with the repr() method relevant to that object.
# Interesting that for strings, the output is wrapped in single quotes.
# Update: %r displays the "raw" data of a variable.  Other conversion operators are used for displaying data to users.
print "I said: %r." % x
# print a string using the String conversion operator which converts any python object using str() for that object.
print "I also said: '%s'." % y

# store a boolean value False into variable hilarious.
hilarious = False
# store a string containing the String conversion operator r% into the variable joke_evaluation.
joke_evaluation = "Isn't that joke so funny?! %r"

#This is pretty interesting since the string formatting / interpolation operator causes the object referenced 
# ...by variable hilarious to be converted by the conversion operator found in string referenced by joke_evaluation variable
print joke_evaluation % hilarious

# store a string in variable w.
w = "This is the left side of..."
# store a string in variable e.
e = "a string with a right side."

#The + operator concatenates when used between two strings.
print w + e
