class stator:
	def __init__(self):
		self.dictionary = [(5,24),(14,19),(9,23),(26,13),(22,7),(20,12),(17,1),(21,25),(16,2),(18,3),(11,8),(10,6),(4,15),(24,5),(19,14),(23,9),(13,26),(7,22),(12,20),(1,17),(25,21),(2,16),(3,18),(8,11),(6,10),(15,4)]

	def find(self, input):
		for i in range(0,26):
			if self.dictionary[i][0] == input:
				return self.dictionary[i][1]
