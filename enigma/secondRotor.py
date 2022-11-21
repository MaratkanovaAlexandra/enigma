def switchDirection(direction):
	return 0 if direction == 1 else 1

class secondRotor:
	def __init__(self):
		self.dictionary = [(18,8),(4,6),(13,5),(23,24),(12,25),(19,21),(2,14),(24,16),(3,19),(7,1),(10,23),(6,2),(20,13),(15,12),(14,10),(5,20),(17,3),(16,17),(9,22),(25,15),(11,18),(8,26),(1,7),(21,9),(22,11),(26,4)]
		self.code_position = 0
		self.decode_position = 0

	def code(self, input, direction):
		self.code_position = self.code_position + 1
		real_position = self.code_position

		search = self.cykleSearch(input + self.cycleItterator(real_position))
		result = 0
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == search:
				result = self.dictionary[i][direction]
		return result

	def decode(self, input, direction):
		self.decode_position = self.decode_position + 1
		
		real_position = self.decode_position
		if direction == 0:
			real_position = real_position + 1
		else:
			real_position = real_position - 1
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == input:
				result = self.dictionary[i][direction] - self.cycleItterator(real_position)
				while result <= 0:
					result = result + 26
		return result

	def cycleItterator(self, itterator):
		while itterator > 26:
			itterator = itterator // 26
		return itterator

	def cykleSearch(self, search):
		while search > 26:
			search = search - 26
		return search
