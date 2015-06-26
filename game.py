from room import Room
from player import Player, choose_character
import cmd

class Game(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.location = Room()
		name,building = choose_character()
		self.player = Player(name,building)
		self.my_character()
		self.look()

	def do_quit(self):
		"""Quits the game"""
		return True

	def my_character(self):
		print("Welcome",self.player.name)
		print("Your building is",self.player.building)

	def look(self):
		print(self.location.description)

	def move(self,direction):
		newroom = self.location._neighbor(direction)
		if newroom is None:
			print("You can't go that way")
		else:
			self.location = newroom #buraya get_room fonksiyonu eklenecek
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