import json

def get_room(id):
	ret = None

	with open(str(id)+".json","r") as f:
		jsontext = f.read()
		d = json.loads(jsontext, strict = False)
		d['id'] = id
		ret = Room(**d)

	return ret

class Room():

	def __init__(self, id=0, name="Unnamed Room", description="Undefined description", neighbors = {}):
		self.id = id
		self.name = name
		self.description = description
		self.neighbors = neighbors

	def _neighbor(self,direction):
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None

