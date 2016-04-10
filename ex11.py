#We put a , (comma) at the end of each print line.  This is so print doesn't end the line with a newline character and go to the next line.

#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()

#print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

#mydata = raw_input('Prompt :')
#print (mydata)


#name=raw_input('Who goes there? : ')
#print "Hi %s, Let us be friends!" %name

## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print "1. Manufactur clones"
print "2. Print money"
print "3. Clean the bottom"
print ("4. Mess around")
print (30 * '-')

is_valid = 0

## Get input ##
while not is_valid:
	try:
		choice = int ( raw_input('Enter your choice [1-3] : ') )
		is_valid = 1
	except ValueError, e :
		print("'%s' is not a valid integer." % e.args[0].split(": ")[0])
		print ("%r" % e)
		
## Take action as per selected menu-option ##
if choice == 1:
	print ("Manufacturing clones...")
elif choice == 2:
	print ("Printing Money...")
elif choice == 3:
	print ("Looking for the hooka rig...")
elif choice == 4: 
	print ("Sharpening spears...")
else:  ## default ##
	print ("Invalid number. Try again...")