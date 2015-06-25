from room import Room
from player import Player
import cmd

class Game(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.location = Room()
		self.player = Player()
		self.my_character()
		self.look()

	def my_character(self):
		print("Welcome ",self.player.name)
		print("Your building is ",self.player.building)

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

	def do_take(self):
		"""Takes an object"""
		pass

	def do_drop(self):
		"""Drops an object"""
		pass


if __name__ == "__main__":
	game = Game()
	game.cmdloop()