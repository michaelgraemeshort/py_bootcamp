import unittest, copy
from cards_exercise import Card, Deck

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", "A")

	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		"""repr should return '<value> of <suit>'"""
		self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""decks should have a cards attribute--a list of length 52"""
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)

	def test_repr(self):
		"""repr should return 'Deck of xx cards'"""
		self.assertEqual(repr(self.deck), "Deck of 52 cards")

	def test_count(self):
		""".count() should return the number of cards in the deck"""
		self.assertEqual(self.deck.count(), 52)

	def test_deal_sufficient_cards(self):
		"""where possible, _deal should remove and return the specified number of cards from the deck"""
		hand = self.deck._deal(10)
		self.assertEqual(len(hand), 10)
		self.assertEqual(self.deck.count(), 42)

	def test_deal_insufficient_cards(self):
		"""otherwise, _deal should remove and return all the cards from the deck"""
		hand = self.deck._deal(100)
		self.assertEqual(len(hand), 52)
		self.assertEqual(self.deck.count(), 0)

	def test_deal_empty_deck(self):
		"""_deal should raise a ValueError when called on an empty deck"""
		self.deck._deal(52)
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_shuffle_full_deck(self):
		"""should shuffle a full deck"""
		unshuffled = copy.copy(self.deck.cards)
		self.deck.shuffle()
		self.assertNotEqual(unshuffled, self.deck.cards)

	def test_shuffle_unfull_deck(self):
		"""should raise a ValueError if called on an unfull deck"""
		self.deck._deal(1)
		with self.assertRaises(ValueError):
			self.deck.shuffle()

	def test_deal_card(self):
		"""should remove and return the last card from the deck"""
		last_card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(last_card, dealt_card)
		self.assertEqual(self.deck.count(), 51)

	# def test_deal_hand(self):
	# 	just calls _deal, already tested above

if __name__ == '__main__':
	unittest.main()