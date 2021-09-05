import unittest
from password import User
from password import Credentials

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
	Another test class that defines test cases for the credentials class.
	"""
	def setUp(self):
		"""A method that runs before each individual credentials test method.
		"""
		self.new_credentials = Credentials('Github','othienoJoe','othieno094!')

	def test_init(self):
		"""
		This is a test case for checking if the credentials instance has been initialized correctly.
		"""
		self.assertEqual(self.new_credentials.account, 'Github')
		self.assertEqual(self.new_credentials.userName, 'othienoJoe')
		self.assertEqual(self.new_credentials.password, 'othieno094!')

	def save_credentials_test(self):
		"""
		Now the test case to test if the object is savedinto the credentials list.
		"""
		self.new_credentials.save_details()
		self.assertEqual(len(Credentials.credentials_list),1)

	def tearDown(self):
		"""
		A method that cleans up after every test case has run
		"""
		Credentials.credentials_list = []

	def test_save_many_accounts(self):
		'''
		A test to check if we can save a multiple credentials objects to the credentials.
		'''
		self.new_credentials.save_details()
		test_credentials = Credentials("Facebook", "NicJoeOtienoz", "dix-9zon")
		test_credentials.save_details()
		self.assertEqual(len(Credentials.credentials_list),2)

	def test_delete_credentials(self):
		"""
		A method to test if an account credentials can be removed from the list
		"""
		self.new_credentials.save_details()
		test_credentials = Credentials("Facebook", "NicJoeOtienoz", "dix-9zon")
		test_credentials.save_details()

		self.new_credentials.delete_credentials()
		self.assertEqual(len(Credentials.credentials_list),1)

	def test_find_credentials(self):
		"""
		Lets check if we can find a credential's entry by account name and display the details of the credential.
		"""
		self.new_credentials.save_details()
		test_credentials = Credentials("Facebook", "NicJoeOtienoz", "dix-9zon")
		test_credentials.save_details()

		the_credentials = Credentials.find_credentials("Facebook")

		self.assertEqual(the_credentials.account, test_credentials.account)