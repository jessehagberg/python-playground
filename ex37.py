Jesse's Python Reference

------------
Keywords  * to practice   ** new
------------
and     Logical and.
		example: True and False == False
		
** as      Part of the with-as statement
		example: with X as Y: pass

** assert  Assert (ensure) that something is true
		example: assert False, "Error!"

*break   Stop this loop right now.
		example: while True: break
		
**class   Define a class
		example:
		class
		Person(object)
		
**continue    Don't process more of the loop, do it again
		example: while True: continue
		
*def:    Define a function
		def X(): pass
		
**del     Delete from dictionary
		example: del X[Y]
		
*elif    Else if condition.
		example: if: X; elif: Y; else: J
		
else    Else condition
		example: if: X; elif: Y; else: J
		
*except  if an exception happens, do this.
		example:
		except ValueError, e:
		print e
		
**exec    Run a string as Python.
		example: exec 'print "hello"'
		
**finally Exceptions or not, finally do this no matter what.
		example: finally: pass
	
*for     Loop over a collection of things.
		example: for X in Y: pass

from    Importing specific parts of a module.
		example: import X from Y
	
**global  Declare that you want a global variable
		example: global X
		
*if      If condition
		example: if: X; elif: Y; else: J
		
import  Import a module into this one to use.
		example: import os
		
*in      Part of for-loops. Also a test of X in Y
		example: for X in Y: pass
		also 1 in [1] == True
		
**is      Like == to test equality.
		example: 1 is 1 == True
		
**lambda  create a short anonymous function
		example:
		s = lambda y: y
		** y; s(3)
		
not     Logical not.
		example: not True == False

or      Logical or.
		example: True or False == True
		
**pass  This block is empty.
		example:
		def empty(): pass
		
print   Print this string
		example: print 'this string'

**raise   Raise an exception when things go wrong.
		example: raise ValueError("No")
		
return  Exit the function with a return value.
		example: def X(): return Y
		
*try     Try this block, and if exception, go to except.
		example: try: pass
		
while   While loop.
		example: while X: pass

**with    With an expression as a variable do.  Also useful as context managers
		example: with X as Y: pass
		Further reading: 
			http://effbot.org/zone/python-with-statement.htm
			http://preshing.com/20110920/the-python-with-statement-by-example/

**yield   Pause here and return to caller.
		example: 
		def X(): yield Y;
		X().next()
		
------------
Data Types  * to practice   ** new
------------

True    True boolean value.
		example: True or False == True
		
False   False boolean value.
		example: False and True == False
		
**None    Represents "nothing" or "no value".
		example: x = None
		
strings Stores textual information
		example: x = "hello"

numbers Stores integers
		example: i = 100
		
floats  Stores decimals
		example: i = 10.389
		
*lists   Stores a list of things.
		example: j = [1,2,3,4]
		
**dicts   Stores a key=value mapping of things.
		example: e = {'x': 1, 'y': 2}

------------
String Escape Sequences
------------
		
\\  Backslash
\'  Single-quote
\"  Double-quote
\a  Bell
\b  Backspace
\f  Formfeed
\n  Newline
\r  Carriage
\t  Tab
\v  Vertical tab
		
------------
String Formats
------------

%d  Decimal integers (not floating point).
	example: "%d" % 45 == '45'
	
%i  Same as %d.
	example: "%i" % 45 == '45'
	
%o  Octal number.
	example: "%o" % 1000 == '1750'

%u  Unsigned decimal.
	example: "%u" % -1000 == '-1000'
	
%x  Hexadecimal lowercase.
	example: "%x" % 1000 == '3e8'
	
%X  Hexadecimal uppercase.
	example: "%X" % 1000 == '3E8'

%e  Exponential notation, lowercase 'e'.
	example: "%e" % 1000 == '1.000000e+03'
	
%E  Exponential notation, uppoercase 'E'.
	example: "%E" % 1000 = '1.000000E+03'
	
%f  Floating point real number.
	example: "%f" % 10.34 == '10.340000'
	
%F  same as %f.
	example: "%F" % 10.34 == '10.340000'
	
%g  Either %f or %e, whichever is shorter.
	example: "%g" % 10.34 == '10.34'
	
%G  Same as %g but uppercase.
	example: "%G" % 10.34 == '10.34'
	
%c  Character format.
	example: "%c" % 34 == '"'
	
%r  Repr format (debugging format).
	example: "%r" % int == "<type 'int'>"
	
%s  String format.
	example: "%s there" % 'hi' == 'hi there'

%%  A percent sign.
	example: "%g%%" % 10.34 == '10.34%'
	
------------
Operators
------------

+   Addition
-   Subtraction
*   Multiplicatin
**  Power of
/   Division
//  Floor division
%   String interpolate or modulus
<   Less than
>   Greater than
<=  Less than equal
>=  Greater than equal
==  Equal
!=  Not equal
<>  Not equal
()  Parenthesis
[ ] List brackets
{ } Dict curly braces
@   At (decorators)
,   Comma
:   Colon
.   Dot
=   Assign equal
;   semi-colon
+=  Add and assign
-=  Subtract and assign
*=  Multiply and assign
/=  Divide and assign
//= Floor divide and assign
%=  Modulus assign
**= Power assign
