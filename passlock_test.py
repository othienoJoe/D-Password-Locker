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

	def test_init(self):
		"""
		It's a test case that checks if the object has been initialized correctly.
		"""
		self.assertEqual(self.new_user.username, 'othienoJoe')
		self.assertEqual(self.new_user.password, 'othieno094!')

	def test_save_user(self):
		"""
		This test helps to know if the new user instance has been saved in the user list.
		"""
		self.new_user.save_user()
		self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
	"""
	Another test class that defines test cases for the credetials class.
	"""
	