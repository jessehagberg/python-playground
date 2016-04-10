"""
A dungeon crawler game about going fishing.  You, our hero, badly want to go
spear fishing at a nearby reef.  It is early in the morning and you must
navigate the maze of activities necessary to make it to the reef.  There are
several tasks that must be performed in order to make it from your comfortable
bed to the promise land of groupers, lobsters and other edible fishes.
"""
from sys import exit
import os

def cls():
	os.system('cls')

class Engine(object):
	"""
	Function to manage game play begining, middle and end.
	"""
	def __init__(self, scene_map):
		self.scene_map = scene_map
		self.moves = 0
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('the_reef')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter(self.moves)
			current_scene = self.scene_map.next_scene(next_scene_name)
			self.moves += 1
			
		#be sure to print out the last scene name
		current_scene.enter(self.moves)
	
class Scene(object):
	"""
	Basic format of each location throughout the game.  Some scenes provide 
	information, others have activities that must be performed and some are
	essentially links from one strategic scene to another.
	"""
	def __init__(self):
		pass
		# Currently unimplemented.
		# self.inventory = {}
		# self.actionItems = {}
		# self.requiredActions = []
	
	def enter(self, moves):
		print "This scene is not yet configured.  Subclass it and implement enter()."
		exit(1)
		
	pass

class Intro(Scene):
	
	def enter(self, moves):
		cls()
		print "*" * 80
		print "You snap awake from a beautiful dream of prowling through deep"
		print "reef canyons filled with diverse flora.  Just before waking"
		print "you'd finished an epic game of cat and mouse with the elder"
		print "grouper by stoning him through a tiny sight hole as"
		print "he made for his back door.  Exhilerated by the experience"
		print "you make up your mind that today was the day to answer the"
		print "ocean's call."
		print "\n"
		print "The challenge at hand is that there are an endless number of steps"
		print "to actually making it out to the reef including familial, work"
		print "and preparatory actions that have to happen before you get to"
		print "glide through those amazing halls of underwater nirvana."
		print "*" * 80
		
		print "-- Moves: %d --" % moves
		action = raw_input("Do you have the courage to try? > ").lower()
		cls()
		
		if "yes" in action:
			print "\n"
			print "Good then let us begin!"
			print "\n"
			return "captains_berth"
		else:
			print "\n"
			print "Yeah, you probably should stay home and do something"
			print "responsible."
			print "\n"
			return "no_fishing_today"
		
		return "captains_berth"
		
class CaptainsBerth(Scene):
	
	def enter(self, moves):
		print "You ease to the edge of the bed in hopes of not waking the"
		print "beautiful goddess that slumbers peacefully beside you.  She"
		print "mumbles something in her sleep and rolls to put her leg over"
		print "yours."
		print "\n"
		print "-- Moves: %d --" % moves		
		action = raw_input("Your move Ace > ").lower()
		cls()
		
		if ("hug" in action) or ("snug" in action):
			if "roll" in action:
				cls()
				print "You expertly perform a hug and roll maneuver while "
				print "gently easing your leg out from under hers.  This day"
				print "is just getting going but you're off to a good start!"
				print "\n"
				return "the_reef"
			else:
				cls()
				print "While a more seasoned veteran would have linked the hug"
				print "with a roll, you decided to snuggle with your fine"
				print "lady. It was totally worth it for some body to body"
				print "contact but don't get any big ideas.  The kids are"
				print "going to be up 5 minutes after raising the wooden flag."
				print "They have some kind of sixth sense about things like"
				print "that."
				print "\n"
				return "no_fishing_today"
				
		elif "hint" in action:
			print "\n"
			print "Jeez pal, we've only been at this for maybe 5 minutes and"
			print "you're already giving up? I might advise a hug, or possibly"
			print "even a hug and roll if I knew about such squishy human"
			print "things."
			print "\n"
			return "captains_berth"
		else:
			print "\n"
			print "DOES NOT COMPUTE! type hint for some possible actions.\n"
			return 'captains_berth'

class NoFishingToday(Scene):
	def enter(self, moves):
		print "Sorry home slice, doesn't look like you're going to make it"
		print "Today. The weather is probably going to suck for the next month"
		print "so you've missed your only chance. You have to bring"
		print "your 'A' game if you are going to roll with the big dogs..."
		print ". um er I mean fish. They tell me that is something humans say."
		print "\n"
		exit(1)

class TheReef(Scene):
	def enter(self, moves):
		cls()
		print "\n"
		print "Great googely moogely.  You made it in %d moves!" % moves
		print "(now don't forget to leave before chomp chomp fin time comes"
		print "around.  Go ahead, live the dream! (You won)"
		return "the_reef"
	
		
# --- --- --- Begin Scenes not yet implemented --- --- ---
class TheHead(Scene):
	
	def enter(self, moves):
		pass
	
class Salon(Scene):

	def enter(self, moves):
		pass

class RadioTable(Scene):

	def enter(self, moves):
		pass

class Galley(Scene):
	
	def enter(self, moves):
		pass

class Cockpit(Scene):
	
	def enter(self, moves):
		pass

class ForeDeck(Scene):

	def enter(self, moves):
		pass

class PortSideWalk(Scene):

	def enter(self, moves):
		pass
	
class StarboardSideWalk(Scene):

	def enter(self, moves):
		pass
		
class Aft(Scene):

	def enter(self, moves):
		pass
		
class SwimPlatform(Scene):

	def enter(self, moves):
		pass

class NoNameHarbour(Scene):

	def enter(self, moves):
		pass

class DinghyCut(Scene):

	def enter(self, moves):
		pass
# --- --- --- End Scenes not yet implemented --- --- ---

class Map(object):
	"""
	A particular map full of scenes with a start scene, a finish scene (win) and a death scene
	"""
	# A list of scenes in this game
	scenes = {
		"intro" : Intro(),
		"captains_berth" : CaptainsBerth(),
		"no_fishing_today" : NoFishingToday(),
		"the_reef" : TheReef(),
		"the_head" : TheHead(),
		"salon" : Salon(),
		"radio_table" : RadioTable(),
		"galley" : Galley(),
		"cockpit" : Cockpit(),
		"port_side_walk" : PortSideWalk(),
		"starboard_side_walk" : StarboardSideWalk(),
		"fore_deck" : ForeDeck(),
		"aft" : Aft(),
		"swim_platform" : SwimPlatform(),
		"no_name_harbour" : NoNameHarbour(),
		"dinghy_cut" : DinghyCut(),		
	}
	
	def __init__(self, start_scene):
		self.startScene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.startScene)

a_map = Map("intro")
a_game = Engine(a_map)
a_game.play()
		

	