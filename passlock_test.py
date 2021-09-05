import unittest
from password import User

class TestClass(unittest.TestCase):
	"""
	This is the Test Class that defines test cases for the user class.
	"""
	def setUp(self):
		"""
		A set up method that runs before each individual test method is finished.
		"""
		self.new_user = User('OthienoJoe', 'othieno094!')

		