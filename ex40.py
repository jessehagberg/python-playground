class Song(object):
		
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

# What am I passing in here?  A String?  Nope... The comma isn't for
#    string concatenation but rather to delimit items in a list.
miss_suzy = Song(["Miss Suzie had a steamboat",
					"The steamboat had a bell",
					"Miss suzie went to heaven",
					"The steamboat went to hell-o..."])
					
miss_suzy.sing_me_a_song()
					
