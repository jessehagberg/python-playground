# import the argv module from the sys package
from sys import argv

#collect the command line paramaters
script, filename = argv

#print a lenghty user prompt using strings and formats
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#await user input (looking for a return)
raw_input("?")

print "Opening the file..."
# retreive a file object withe write mode enabled
#target = open(filename, 'w')
target = file(filename, 'w')
print "Truncating the file.  Goodbye!"
# truncate the file by calling the truncate() function of the file object.
#  Note: truncate is not necessary when the file is opened in 'w' (write) mode since the file is truncated automatically.
#        If the file were opened in 'a' append mode it could be truncated
#        Adding the '+' modifier to 'w' or 'a' opens in read or write mode.
target.truncate()

print "Now I'm going to ask you for three lines."

# Collect three lines of input from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

## Write 6 strings to the file.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#Eliminate repetition and write the data using strings, formats and escapes.
target.write("%s\n%s\n%s\n" % (line1, line2, line3))


print "And finally, we close it."
# Close the file
target.close()

