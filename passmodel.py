#! /usr/bin/env python3.9
from password import User, Credentials

def function():
	print("  __            _                                     ")
	print(" |    \        | |        ____      ____   _    _     ")
	print(" |  |  ) ===   | |       /  _  \   /  __\ | |__//     ")
	print(" |  |  ) ===   | |____  |  |_|  | |  (___ | |__/\     ")
	print(" |___ /        |______|  \____ /   \____/ |_|  \_\    ")
function()

def create_new_user(username, password):
	"""
	We've created a function to create a new user with the username and password.
	"""
	new_user = User(username, password)
	return new_user

def save_user(user):
	"""
  This function to save a new user
	"""
	user.save_user()

def display_user():
	"""
	A function to display existing user.
	"""
	return User.delete_user()

def login_user(username, password):
	"""
	This function checks whether a user exist and login the user in
	"""
	check_user = Credentials.verify_user(username, password)
	return check_user

def create_new_credentials(account, userName, password):
	"""
	We have created another function that creates new credentials for a given user account.
	"""
	new_credentials = Credentials(account, userName, password)
	return new_credentials

def save_credentials(credentials):
	"""
	A function to save Credentials to the credentials list
	"""
	credentials.save_details()

def display_accounts_details():
	"""
  This function returns all the saved credentials
	"""
	return Credentials.display_credentials()
