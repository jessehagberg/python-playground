#Exercise 20: Functions and Files
# import the argv module from the sys package
from sys import argv

#unpack the command line arguments
script, input_file = argv

# define a method that prints a whole file
def print_all(f):
	# output of [file].read() function is sent to print command
	print f.read()
	
# define a method that resets the file marker
def rewind(f):
	#call the [file].seek() method passing zero as an argument
	# this causes the file marker to go back to the beginning of the open file.
	f.seek(0)

# print the next line from a file along with a count that is passed in.
# The does something useful but seems very manual.
def print_a_line(line_count, f):
	#display the integer passed in on "line_count" argument concatenated by the comma
	# with the output from the [file].readline() method.
	#first pass... current_line becomes line_count: 1
	#second pass... current_line becomes line_count: 2
	#third pass... current_line becomes line_count: 3
	print line_count, f.readline()

# get a file object by opening the file named by the input_file string variable (that came from argv)
current_file = open(input_file)

print "First let's print the whole file:\n"

# call the print_all function, passing in the file object
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# call the rewind function, passing in an opened file object.
rewind(current_file)

print "Let's print three lines:"

# store the integer one in a named variable "current_line"
current_line = 1
# call the print_a_line method passing in the integer just created and an opened file object.
#current_line: 1
print_a_line(current_line, current_file)

# increment the current_line variable by 1
#current_line = current_line + 1
#First use of the += construct
current_line += 1;
# current_line: 2
# call the print a line method again
print_a_line(current_line, current_file)

# increment the current_line variable by 1
#current_line = current_line + 1
current_line += 1;
# current_line: 3
# call the print_a_line method a third time
print_a_line(current_line, current_file)
