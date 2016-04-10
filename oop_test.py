import random
from urllib import urlopen
from sys import argv

# URL for downloading an online list of random words, one per line.
WORD_URL = "http://learncodethehardway.org/words.txt"

# Create an empty list named WORDS.
WORDS = []

# Create a dictionary with name:value pairs composed of 1) a code snippet and 2) the english description of that code.
# Each string has special character strings we will replace later based on random words.
# %%% class names
# *** other names
# @@@ parameter names
PHRASES = {
	"class %%%(%%%):":"Make a class named %%% that is-a %%%.",
	"class %%%(object:\n\tdef __init__(self, ***):" : "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@):":"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":"Set *** to an instance of class %%%.",
	"***.***(@@@)":"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(argv) == 2 and argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# Load up the words from the website
# urlopen opens a socket connection to the given URL.  The readlines() method gets all lines from this socket.
for word in urlopen(WORD_URL).readlines():
	#trim off the leading and trailing characters (whitespace by default) and then append to a list called WORDS.
	WORDS.append(word.strip())
	
#create a function named convert that accepts two strings, snippet and phrase	
def convert(snippet, phrase):
	# inside out here...
	#   snippet.count("%%%") counts the occurrances of the string "%%%" within the string object named snippet.
	#   next the sample function is retrieved from the random module and passed 
	#       parameters WORDS (a list) and the number of occurances of '%%%' that need to be replaced
	#		random.sample() returns a list
	#   next an iterator is run over the output of random.sample, each returned word is capitalized by string.capitalize()
	#   this output is returned in a list and assigned to a variable called class_names
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("%%%"))]
	# create a new random list of words based on how many times '***' is found in snippet and assign to variable other_names
	other_names = random.sample(WORDS, snippet.count("***"))
	
	#create empty lists named results and param_names
	results = []
	param_names = []
	
	#If parameters are called for, generate between 1 and 3 of them and store in a list named param_names
	# iterate through the number of times the string "@@@" is found in the snippet.
	for i in range(0, snippet.count("@@@")):
		# generate a random number among 1, 2 or 3 and store in a variable named  param_count
		param_count = random.randint(1,3)
		# join a random sample of words with commas and append the resulting string to a list variable named param_names
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	#for each of the snippet and phrase, do stuff
	for sentence in snippet, phrase:
		#copy the sentence content (copy a list) (even though it's a string) into a new list or string.
		result = sentence[:]
		
		# fake class names
		# replace all the '%%%' found with class_names words
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# fake other names
		# replace all the '***' found with other_names words.
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		# replace all the '@@@' found with param_names words.
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		# append the result to a list called results
		results.append(result)
		
	# return the updated versions of snippet and phrase.	
	return results
	
#keep doing this forever.
while True:
	# get all keys for the PHRASES dict and assign to the list named snippets.
	snippets = PHRASES.keys()
	#shuffle the snippets list
	random.shuffle(snippets)

	#for each snippet (these are shuffled keys remember?)
	for snippet in snippets:
		#retrieve the corresponding phrase
		phrase = PHRASES[snippet]
		#convert the snippet and phrase then assigne them to question and answer.
		question, answer = convert(snippet, phrase)
		#swap them if necessary
		if PHRASE_FIRST:
			question, answer = answer, question
			
		#print the question
		print question
		
		#make the monkey press a key
		raw_input("> ")
		
		#show the answer
		print "ANSWER:  %s\n\n" % answer
			
			
	
		
			
