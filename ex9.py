# Here's some new strange stuff, remember type it exactly

# Create a string of days delimited by spaces
days = "Mon Tue Wed Thu Fri Sat Sun"
# Create a string of months deliminted by newlines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#concatenating two strings and printing them, noticing the spacing.
print "Here are the days: ", days
#concatenating two strings and printing them, noticing the spacing.
print "Here are the months: ", months

#Here we're using a construct where we can type multiple lines without having to terminate them with double quotes.
#  .... this is equivalent to {{{ }}} in JSPWiki
print """
There's something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""