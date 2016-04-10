from sys import argv

script, file_name = argv

txt = open(file_name)

print "We're about to work with a file called %r" % file_name
print "Here goes!"
print "Are you ready yet?"

print txt.read()

print "There it is.  Now closing the file for good measure."
txt.close()