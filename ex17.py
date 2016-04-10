# import the argv module from the sys package
from sys import argv
# import the exists module from the os.path package
from os.path import exists

# unpack the command line arguments
#script, from_file, to_file = argv

open(argv[2],'w').write(open(argv[1]).read())
