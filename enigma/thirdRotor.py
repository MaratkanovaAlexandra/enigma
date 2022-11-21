def switchDirection(direction):
	return 0 if direction == 1 else 1

class thirdRotor:
	def __init__(self):
		self.dictionary = [(1,3),(5,20),(17,2),(2,15),(14,18),(8,1),(12,13),(18,10),(9,5),(13,24),(3,19),(23,6),(6,17),(16,12),(25,21),(15,26),(4,8),(10,25),(21,9),(26,14),(22,11),(19,16),(11,23),(24,7),(7,4),(20,22)]
		self.code_position = 0
		self.decode_position = 0

	def code(self, input, direction):
		self.code_position = self.code_position + 1
		if self.code_position > 26:
			self.code_position = self.code_position - 26
		search = self.cykleSearch((input + self.code_position))
		result = 0
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == search:
				result = self.dictionary[i][direction]
		return result

	def decode(self, input, direction):
		self.decode_position = self.decode_position + 1
		if self.decode_position > 26:
			self.decode_position = self.decode_position - 26
		real_position = self.decode_position
		if direction == 0:
			real_position = real_position + 1
		else:
			real_position = real_position - 1
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == input:
				result = self.dictionary[i][direction] - real_position
				while result <= 0:
					result = result + 26
		return result

	def cykleSearch(self, search):
		while search > 26:
			search = search - 26
		return search
