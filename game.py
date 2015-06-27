from room import Room, get_room
from player import Player, choose_character,house_mottos
import cmd
import textwrap

class Game(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.location = get_room(1)
		name,building = choose_character()
		self.player = Player(name,building)
		self.my_character()
		self.look()

	def do_quit(self):
		"""Quits the game"""
		return True

	def my_character(self):
		print("Your choice is {0}".format(self.player.building))
		print("Always remember :  {0}".format(house_mottos[self.player.building]))

	def look(self):
		print("")
		print(self.location.name)
		for line in textwrap.wrap(self.location.description,width=75):
			print(line)

	def move(self,direction):
		newroom = self.location._neighbor(direction)
		if newroom is None:
			print("You can't go that way")
		else:
			self.location = get_room(newroom) #buraya get_room fonksiyonu eklenecek
			self.look()

	def do_neighbors(self):
		""" Shows all the neighbors with respect to your current position"""
		pass

	def do_n(self):
		"""Go North"""
		pass

	def do_s(self):
		"""Go South"""
		pass

	def do_w(self):
		"""Go West"""
		pass

	def do_e(self):
		"""Go East"""
		pass

	def do_up(self):
		"""Go Up"""
		pass

	def do_down(self):
		"""Go Down"""
		pass
"""
	def do_take(self,item):
		pass

	def do_drop(self,item):
		pass
"""

if __name__ == "__main__":
	game = Game()
	game.cmdloop()