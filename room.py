def get_room():
	pass

class Room():

	def __init__(self, id=1, name="Unnamed Room", description="Undefined description", neighbors = {}):
		self.id = id
		self.name = name
		self.description = description
		self.neighbors = neighbors

	def _neighbor(self,direction):
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None

