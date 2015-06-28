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

	def do_quit(self, args):
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

	def do_neighbors(self,args):
		""" Shows all the neighbors with respect to your current position"""
		print(self.location.neighbors)

	def do_n(self,args):
		"""Go North"""
		self.move('n')

	def do_s(self,args):
		"""Go South"""
		self.move('s')

	def do_w(self,args):
		"""Go West"""
		self.move('w')

	def do_e(self,args):
		"""Go East"""
		self.move('e')

	def do_up(self,args):
		"""Go Up"""
		self.move('u')

	def do_down(self,args):
		"""Go Down"""
		self.move('d')
"""
	def do_take(self,item):
		pass

	def do_drop(self,item):
		pass
"""

if __name__ == "__main__":
	game = Game()
	game.cmdloop()