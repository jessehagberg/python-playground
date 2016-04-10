fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

skinny_cat = '''
Here's another list:
\t* mice
\t* cochroaches
\t* dryer lint
'''


#This exercise shows how to put escaped characters into a string, namely newlines and tabs.
print fat_cat
print skinny_cat

#Build up a grand format string containing escape sequences
myFormat = '''Title: %s\nDescription: %s\nList Of Actors:\n%s'''

title = "These Are The Days of Our Lives"
description = "Mon Tue Wed Thu Fri Sat Su"
actorFormat = "\t* %r\n\t* %r\n\t* %s"
actors = actorFormat % ("Jesse", "\"Bethany\"", "\"Noah\"")

print actors
print myFormat % (title, description, actors)



