# import the 'argv' module from the sys package
from sys import argv

#unpack the script name and first command line parameter into variables
script, filename = argv

# retrieve a file object that references file named by 'filname' variable
txt = open(filename)

# print the name of the file passed in on the command line
print "Here's your file %r:" % filename
#print the contents of the file using the read() function/method
print txt.read()
txt.close()

# print instructions for the user
print "Type the filename again: "
# collect user input
file_again = raw_input("> ")

# retrieve a file object referencing the file passed in via a prompt
txt_again = open(file_again)

# print the contents of the file
print txt_again.read()
txt_again.close()

#Q: Why is getting the filename better one way or the other?
#A: In some cases the relevant filenames may be known before the program is run.  In this case the command line argument is better.
#   In other cases, the user may want to specify the file name while the program is running.  In this case a user prompt is best.
