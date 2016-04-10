 # Create a string that containing string formatting conversion flags
formatter = "%r %r %r %r"

#Prints 4 integers as converted through the format string referenced by variable 'formatter'
print formatter % (1, 2, 3, 4)
#Prints 4 strings as converted through the format string 'formatter'
print formatter % ("one", "two", "three", "four")
#Prints 4 boolean values as converted through the format string 'formatter'
print formatter % (True, False, False, True)
#Prints 4 strings as converted through the format string 'formatter'. 
#   ... the string 'formatter' is treated as a literal string on the right hand side of the formatting/interpolation operator 
print formatter % (formatter, formatter, formatter, formatter)
# print 4 longer strings as converted through the format string 'formatter'
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
	