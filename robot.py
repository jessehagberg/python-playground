name = raw_input("\nWhat is your name? ")
count = 0

while True:
	if(count = 0):
		food = raw_input("\n%s, what is your favorite food? " % name)
	else:
		food = raw_input("Do you have any other favorite foods? ")

	if ("spaghetti" in food.split(' ') or "sushi" in food.split(' ')):
		print "\nI'm sorry %s, my planet just split in two.  I have to go now." % name
	else:
		print "\nDon't worry %s, my Mom is going to make %s tonight!" % (name, food)
		
	count += 1

while False:
	todo = raw_input("\n\nHi %s, what would you like me to do? " % name)

	if ( "robot" in todo.split(' ')):
		print "I'm sorry %s, I tried to %s and my whole planet was destroyed.  Please don't ask me to do it again!" % (name, todo)
	elif( "shark" in todo.split(' ') or "elephant" in todo.split(' ')):
		print "Well %s, I've got a pretty tight schedule.  I can't %s right now.  Bye!" % (name, todo)
	elif( "horse" in todo.split(' ')):
		print "Oh %s, I happen to have one of those in my back yard that you can have for free!" % name
	else:
		print "Ok %s, no problem.  I'll get my computer processor brain working on %s right away!" % (name, todo)