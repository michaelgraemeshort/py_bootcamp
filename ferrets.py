import pickle

class Ferret:
	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __str__(self):
		return f"{self.size} ferret called {self.name}."

	def poke(self):
		return f"{self.name} bit you!"

gnasher = Ferret("Gnasher", "Large")
print(gnasher.__dict__)
# gnipper = Ferret("Gnipper", "Small")

# print(gnasher)
# print(gnipper.poke())

# with open("ferrets.pickle", "wb") as file:
# 	pickle.dump(gnasher, file)

# with open("ferrets.pickle", "rb") as file:
# 	gnasher = pickle.load(file)

# print(gnasher.poke())