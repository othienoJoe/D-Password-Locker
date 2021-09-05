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

	@classmethod
	def display_user(cls):
		return cls.user_list

	def delete_user(self):
		"""
		A method that removes completely the saved account from the list.
		"""
		User.user_list.remove(self)

class Credentials():
	"""
	A new credentials class that helps create new objects of credentials.
	"""
	credentials_list = []
	@classmethod

	def verify_user(cls, username,password):
		"""
		This method verifies whether the user is in the user_list or not.
		"""
		a_user = ""
		for user in User.user_list:
			if(user.username == username and user.password == password):
				a_user == user.username
		return a_user

	def __init__(self, account, userName, password):
		"""
		A method that defines the user credentials to be stored
		"""
		self.account = account
		self.userName = userName
		self.password = password
  
	def save_details(self):
		"""
		This is a method that stores the new credentials to the credentials
		"""
		Credentials.credentials_list.append(self)

	def delete_credentials(self):
		"""
		This method deletes an account's credentials from the credentials_lists
		"""
		Credentials.credentials_list.remove(self)

	@classmethod
	def find_credentials(cls, account):
		"""
    Another class method that takes in an account name and returnsthe credentials that match the needed account name
		"""
		for credentials in cls.credentials_list:
			if credentials.account == account:
				return credentials

	@classmethod
	def copy_password(cls, account):
		"""
		This class method copies the object in the list
		"""
		found_credentials = Credentials.find_credentials(account)
		pyperclip.copy(found_credentials.password)
		
