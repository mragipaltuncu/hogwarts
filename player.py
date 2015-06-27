def choose_character():
	"""Choose your character"""
	name = input("What is your name student ?: ")
	print("")
	print("It is our choices {0}, that show us who we truly are,\nfar more than our abilities -- Albus Dumbledore".format(name))
	print("")
	while True:
		print("Which Hogwarts House do you want to choose?")
		print("""
		1-Gyriffindor
		2-Slytherin
		3-Ravenclaw
		4-Hufflepuff
		""")
		building = input("Choose : ")
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

house_mottos = {"Gyriffindor":"Their daring, nerve and chivalry set Gryffindors apart",
				"Slytherin":"Slytherin will help you on your way to greatness",
				"Hufflepuff":"Those patient Hufflepuffs are true and unafraid of toil",
				"Ravenclaw":"Wit beyond measure is man's greatest treasure"}

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
