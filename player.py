def choose_character():
	"""Choose your character"""
	pass

class Player():

	def __init__(self,id=1,name="Player's Name",building="Player's Building",items=[]):
		self.id = id
		self.name = name
		self.building = building
		self.items = items

	def take_item(self,item):
		if item not in self.items:
			print("Added ",item,"to your items")
			self.items.append(item)
			return items
		else:
			print("You already have that item!")
			return None

	def drop_item(self,item):
		if item in self.items:
			print("Dropped ",item)
			self.items.remove(item)
			return items
		else:
			print("You don't have that item")
			return None

