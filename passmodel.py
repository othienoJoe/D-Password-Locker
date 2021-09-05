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

	"""
