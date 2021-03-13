class Robot(object):
    moves = {"N":[0, 1], "S":[0, -1], "E":[1, 0], "W":[-1, 0]}
	lastMoves = []
	def __init__(self, coors):
		self.x = coors[0];
		self.y = coors[1];
		self.lastMoves = [(self.x, self.y)]
	def move(self, stringCommands):
		self.lastMoves = [(self.x, self.y)]
		for l in stringCommands:
			self.x += self.moves[l][0];
			self.y += self.moves[l][1];
			self.lastMoves.append((self.x, self.y))
		return (self.x, self.y);
	def path(self):
		return self.lastMoves
