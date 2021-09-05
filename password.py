import random
import string
import pyperclip

class User:
	"""
	Create user class that generates new instances for a user.
	"""
	user_list = []

	def __init__(self, username, password):
		"""
		A method that defines the properties of the user.
		"""
		self.username = username
		self.password = password

	def save_user(self):
		"""
		To save the new user instance into the user list.
		"""
		User.user_list.append(self)

		