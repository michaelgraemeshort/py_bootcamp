import random

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		# return f"{self.value} of {self.suit}"
		return "{} of {}".format(self.value, self.suit)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(suit, value) for suit in suits for value in values]

	def __repr__(self):
		# return f"Deck of {self.count()} cards"
		return "Deck of {} cards".format(self.count())

	def count(self):
		return len(self.cards)

	def _deal(self, number_of_cards):
		total = self.count()
		actual = min([total, number_of_cards])
		if total == 0:
			raise ValueError("All cards have been dealt")
		else:
			hand = [self.cards.pop() for i in range(actual)]
			return hand

	def shuffle(self):
		if self.count() == 52:
			random.shuffle(self.cards)
			return self.cards
		else:
			raise ValueError("Only full decks can be shuffled")

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, number_of_cards):
		return self._deal(number_of_cards)