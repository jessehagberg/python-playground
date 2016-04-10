from sys import argv

script, ballcolor, ballsize = argv

print "You have really %s %s balls!" % (ballcolor, ballsize)

ballcount = int(raw_input("How many more would you like? : "))

print ("ok, you would prefer to have %d more %s %s balls!" % (ballcount, ballcolor, ballsize))