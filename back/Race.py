class Car(object):
	oils = {98: 1, 95: 0.9, 92: 0.8}
	"""docstring for Car"""
	def __init__(self, number, speed, oil):
		self.number = number
		self.speed = speed * self.oils[oil]

	def getPosition(self, M, t):
		# return {self.number: int(M - t * self.speed % M)}
		return int(M - t * self.speed % M)

class Moto(Car):
	"""docstring for Moto"""
	oils = {98: 1, 95: 0.8, 92: 0.6}

class Guzh(Car):
	"""docstring for Moto"""
	def __init__(self, number, speed):
		self.number = number
		self.speed = speed

f = open('input.txt')
data = f.readline().replace('\n', '').split(' ')
N = int(data[0])
M = int(data[1])
t = int(data[2])
racers = {}
for i in range(N):
	item = f.readline().replace('\n', '').split(' ')
	if int(item[1]) == 1:
		racer = Car(int(item[0]), int(item[2]), int(item[3]))
		# racers.append(racer.getPosition(M, t))
		racers[int(item[0])] = racer.getPosition(M, t)
	if int(item[1]) == 2:
		racer = Moto(int(item[0]), int(item[2]), int(item[3]))
		# racers.append(racer.getPosition(M, t))
		racers[int(item[0])] = racer.getPosition(M, t)
	if int(item[1]) == 3:
		racer = Guzh(int(item[0]), int(item[2]))
		# racers.append(racer.getPosition(M, t))
		racers[int(item[0])] = racer.getPosition(M, t)
	# if 
# print(N, M, t)
# print(racers)
minval = min(racers.values())
# print(minval)
res = [k for k, v in racers.items() if v==minval]
print(min(res))
# [321, 323]
# print(min(racers, key=racers.get))
