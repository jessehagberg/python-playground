# -- Functions
# functions do 3 things
# 1. name pieces of code the way variables name strings and numbers
# 2. They take arguments the way your scripts take argv
# 3. Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands"

#   def

#   create a function beginning with the word "def"

# this one is like your scripts with argv
def print_two(*meh):
	arg1, arg2 = meh
	print "arg1: %r, arg2: %r meh" % (arg1, arg2)
	
#ok, that #args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
	
def print_none():
	print "I got nothin'."


	
print_two("Jesse", "Two Many ARgs")
print_two_again("Jesse Too Few Args","ok, ok")
print_one("Fine.")
