question = "What is your name? "

name = raw_input(question)

print "Hi %s, Nice to meet you!" % name

question = "What is your favorite food? "

food = raw_input(question)

if (food == "pizza"):
	print "Oh, I love pizza too, %s!" % name
elif (food == "jelly beans"):
	print "Oh, I looooove jelly beans, %s!" % name
else: 
	print "%s, I have no earthly idea what %s is but I bet it's horrible!" % (name, food)
