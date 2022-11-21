def switchDirection(direction):
	return 0 if direction == 1 else 1

class firstRotor:
	def __init__(self):
		self.dictionary = [(24,19),(19,20),(5,13),(6,7),(2,5),(15,25),(8,17),(9,4),(20,10),(12,11),(25,23),(11,6),(18,8),(23,2),(21,16),(16,26),(26,1),(7,21),(3,3),(4,12),(14,15),(22,9),(17,24),(13,22),(1,14),(10,18)]
		self.code_position = 0
		self.decode_position = 0

	def code(self, input, direction):
		self.code_position = self.code_position + 1
		real_position = self.code_position

		search = self.cykleSearch(input + self.cycleItteratorSqrt(real_position))
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
				result = self.dictionary[i][direction] - self.cycleItteratorSqrt(real_position)
				while result <= 0:
					result = result + 26
		return result

	def cycleItteratorSqrt(self, itterator):
		if itterator // (26*26) > 1:
			while itterator > (26*26):
				itterator = itterator // (26*26)
		else:
			itterator = itterator // (26*26)
		return itterator

	def cykleSearch(self, search):
		while search > 26:
			search = search - 26
		return search
