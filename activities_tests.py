import unittest
from activities import eat, nap, is_funny, laugh

class ActivitiesTests(unittest.TestCase):
	def test_eat_bool(self):
		"""eat should raise a ValueError if is_healthy is not a Boolean"""
		with self.assertRaises(ValueError):
			eat("spam", "who cares?")

	def test_eat_healthy(self):
		"""eat should return a smug message if is_healthy == True"""
		self.assertEqual(
			eat("broccoli", True), 
			"I'm eating broccoli, because my body is a temple"
		)
	def test_eat_unhealthy(self):
		"""eat should return a carefree message if is_healthy == False"""
		self.assertEqual(
			eat("pizza", False),
			"I'm eating pizza, because YOLO!"
		)
	def test_short_nap(self):
		"""nap should return a positive message if num_hours == 1"""
		self.assertEqual(
			nap(1),
			"I'm feeling refreshed after my 1 hour nap"
		)
	def test_long_nap(self):
		"""nap should return a distressed message if num_hours != 1"""
		self.assertEqual(
			nap(3), 
			"Ugh, I overslept. I didn't mean to nap for 3 hours!",
			"here is a message that will be displayed if this test fails"
		)
	def test_is_funny_tim(self):
		"""tim should return False"""
		self.assertFalse(is_funny("tim"), "here is another error message, displayed on failure")

	def test_is_funny_anyone_else(self):
		"""anyone other than tim should return True"""
		self.assertTrue(is_funny("jim"))

	def test_laugh(self):
		"""should return haha or lol"""
		self.assertIn(laugh(), ("haha", "lol"))


if __name__ == "__main__":
	unittest.main()