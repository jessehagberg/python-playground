#Exercise 22: What do you know so far?

print
-- String Delimiters, operators, conversion and formatting
""
''
"'"
'"'
\[char]         escape sequences \n for newline \t for tab, etc...

-- String methods
[string].split

-- command line arguments
from sys import argv
argv
script, arg1 = argv

-- user input
raw_input(["prompt"])

-- type casting
int()
float()

-- importing modules from packages
from [package] import [module]

"""[multi-line text]""" construct for specifying multi-line strings
'''[multi-line text]''' Another way to do it.

-- format strings
#
,               String concatentation operator, field delimiter
print "blah",   
%               conversion operator
%d              integer (digits) conversion format flag
%s              string conversion format flag
%r              representation conversion format flag
"a","r" * 10, "g", "h" * 3
+               precise concatenation operator
,               concatenation operator inserting a space between strings

-- Variable types
int         100
float       100.0

-- Mathematic and logial operators
+               Addition operator
-               Subtraction operator
*               multiplication operator
\               Division operator               
%               modulo
<               Less than
>               Greater than
>=              Greater than or equal to
<=              Less than or equal to
==              Comparison operator (string comparison is case sensitive)
-2              negative numbers
=               Assignment operator
variable_name_syntax

-- Looping structures
while
while not

-- exception handling
try:
except ValueError, e :
[exception].args

-- conditional structures
if:
elif:
else:

-- file class
open(filename[,("r" | "w" | "a")])
[file].read()
[file].seek()
[file].readline()
[file].close()
[file].truncate()
[file].write()
how to copy one file to another

-- functions
def [function_name]([arg(s)]):  
function input parameters
function return values


