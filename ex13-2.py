#Import the argv variable from the sys module
from sys import argv

#unpack the command line arguments
script, bungeecount, bungeecolor = argv


#print out a funny sentence incorporating the two arguments given.
print "There are too many" + bungeecolor, "bungee cords", \
	"in my boat! I only need", bungeecount, "of them."
	
#Get user input.  an answer to a question.
giveaway = raw_input("Would you like to give some away? : ")

#Print out a message depending on the user's answer
if giveaway == "yes":
	print "Great!  No problem!"
elif giveaway == "no":
	print "Then stop complaining already."
else:
	print "yeah, not sure what you said there.  Enjoy yer bungees!"