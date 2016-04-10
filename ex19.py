from sys import argv

script, argMahi, argTuna, argSnapper, argLobster, argBarracuda = argv

# exercise 19: functions and variables

#create a function named 'cheese_and_crackers' that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#print out the first argument with some conTEXT and formatting
	print "You have %d cheeses!" % cheese_count
	#print out the second argument with some conTEXT and formatting
	print "You have %d boxes of crackers!" % boxes_of_crackers
	
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# call our function and pass two integer arguments directly
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
# create two integer variables
amount_of_cheese = 10
amount_of_crackers = 50

# call our function using the variables we just created that reference integers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# showing that I can do math inside the function argument call area
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# showing that I can use a combination of variable names and math inside the function argument payload
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def fish_report(numMahi, numTuna, numSnapper, numLobster, numBarracuda, others):
	print "Wow, you caught %r Mahi Mahi so far!" % numMahi
	print "... and %r Tuna?!! You are a fishing god!" % numTuna
	print "I bet you haven't caught any other kinds of fish though."
	print "What? %r Snapper, %r Spiny Lobster and %r Barracuda and %s?" % (numSnapper, 
	numLobster, numBarracuda, others)
	print"  You are talented my friend. Congratulations!\n"

print "Here we call our function with specific numbers passed directly as arguments to the function"
fish_report(2, 2, 4, 5, 7, "some other fish")

print "1: Call our function using math"
fish_report(0+1+1+0,1+1,1+1+1+1,2+3,1+1+1+1+1+1+1+1,"some other fishes")

mahi, tuna, snapper, lobster, barracuda = (5, 4, 3, 2, 1)
print "2: Calling our function using variables"
fish_report(mahi, tuna, snapper, lobster, barracuda, "three types of grouper")

print "3: calling our function using a combination of variables and math"
fish_report(mahi + 1, tuna + 1, snapper - 1, lobster - 1, barracuda +5, "rock hinds")

print "Calling function using command line arguments"
fish_report(int(argMahi), int(argTuna), int(argSnapper), int(argLobster), int(argBarracuda), "red hinds")

print "ok, let's get real here.  What other types of fish have you caught?"
prompt = ">"
inputFishCaught = raw_input(prompt)
print "4: Wow ten is going to be a lot of work! user input used on this round."
fish_report(1, 2, 3, 4, 5, inputFishCaught)

print "5: Math + command line args"
fish_report(int(argMahi) * 10, int(argTuna) * 10, int(argSnapper) * 10, int(argLobster) * 10, int(argBarracuda) * 10, "and many others x 10 :o)")

print "6: Math + command line args + user input"
fish_report(int(argMahi) * 100, int(argTuna) * 100, int(argSnapper) * 100, int(argLobster) * 100, int(argBarracuda) * 100, inputFishCaught)

print "7: User Input + string replication"
fish_report(55 / 5, 44 / 4, 33 / 3, 22 / 2, 11 / 1, "Hi Mom! " * 20)

print "8: Honing in on the goal line"
fish_report(int(argMahi) * 1000, 2000, "a lot of", "about a million", "not enough", inputFishCaught)

prompt = "How many %s did you say?: "
print "9: getting crazy here"
fish_report(int(raw_input(prompt % "Mahi")), 2, 3, 4, 5, inputFishCaught)

print "10: The finish line is in sight!"
fish_report(int(raw_input(prompt % "Mahi")), int(raw_input(prompt % "Tuna")),
	int(raw_input(prompt % "Snapper")), raw_input(prompt % "Lobster"),
	raw_input(prompt % "Barracuda"), inputFishCaught)

