def choose_character():
	"""Choose your character"""
	name = input("Name your character : ")

	while True:
		print("What building do you want to choose?")
		print("""
		1-Gyriffindor
		2-Slytherin
		3-Ravenclaw
		4-Hufflepuff
		""")
		building = input()
		if building == "1":
			building = "Gyriffindor"
			break
		elif building == "2":
			building = "Slytherin"
			break
		elif building == "3":
			building = "Ravenclaw"
			break
		elif building == "4":
			building = "Hufflepuff"
			break
		else:
			print("Choose wisely!")
		
	return (name,building)

class Player():

	def __init__(self,name="Player's Name",building="Player's Building"):

		self.name = name
		self.building = building
	
"""
# will add item system in the future
# player actions

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
"""
