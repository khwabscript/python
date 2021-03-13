class PearsBasket(object):

	def __init__(self, numPears):
		self.numPears = numPears

	def __str__(self):
		return str(self.numPears)

	def __repr__(self):
		return self.__class__.__name__ + '(' + str(self.numPears) + ')'

	def __floordiv__(self, delimiter):
		baskets = []
		for i in range(0, self.numPears // delimiter):
			baskets.append(PearsBasket(self.numPears // delimiter))
		if self.numPears % delimiter > 0:
			baskets.append(PearsBasket(self.numPears % delimiter))
		return baskets

	def __mod__(self, delimiter):
		return self.numPears % delimiter

	def __add__(self, item):
		return PearsBasket(self.numPears + item.numPears)

	def __sub__(self, n):
		self.numPears = max(0, self.numPears - n)
