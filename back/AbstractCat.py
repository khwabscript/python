class AbstractCat(object):
	def __init__(self):
		self.weight = 0
		self.remainder = 0
		pass

	def __str__(self):
		return self.__class__.__name__ + ' (' + str(self.weight) + ')'

	def eat(self, kg):
		self.weight += kg // 10
		self.remainder += kg % 10

		if self.remainder > 9:
			self.weight += 1
			self.remainder -= 10

		if self.weight > 100:
			self.weight = 100

class Kitten(AbstractCat):
	def __init__(self, weight):
		self.weight = weight
		self.remainder = 0

	def meow(self):
		return "meow..."

	def sleep(self):
		return 'Snore' * (self.weight // 5)

class Cat(Kitten):
	def __init__(self, weight, name):
		Kitten.__init__(self, weight)
		self.name = name

	def meow(self):
		return "MEOW..."

	def get_name(self):
		return self.name

	def catch_mice(self):
		return 'Got it!'
