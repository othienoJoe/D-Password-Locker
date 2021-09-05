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

def delete_credentials(credentials):
	"""
	A function  that deletes a Credential from credentials list
	"""
	credentials.delete_credentials()
	
def find_credentials(account):
	"""
	This function finds the credentials by an account name retursns the credential.
	"""
	return Credentials.find_credentials(account)

def check_credentials(account):
	"""
	To check if a Credentials exist with that account name and return a boolean.
	"""
	return Credentials.if_credentials_exist(account)

def generate_password():
	"""
	This function generates a random password for the user.
	"""
	auto_password = Credentials.generatePassword()
	return auto_password

def copy_password(account):
	"""
	Another function that copies the password using the pyperclip framework by importing the framework .
	"""
	return Credentials.copy_password(account)


def passlock():
	print("Hello and Welcome to your Account's Password Lock...\n Please enter one of the following to proceed.\n CA --- Create New Account  \n LI  ---  Already Have An Account  \n")
	short_code = input("").lower().strip()
	if short_code == "ca":
		print("Sign Up")
		print('*' * 50)
		username = input("User_name: ")
		while True:
			print(" TP - To type personal password:\n GP - To generate random Password")
			if password_choice == 'tp':
				password = input("Enter Password\n")
				break
			elif password_Choice == 'gp':
				password = generate_password()
				break
			else:
				print("Invalid password please try again")
		
		save_user(create_new_user(username, password))
		print("*"*85)
		print(f"Hello {username}, Your account has successfully! Your password is: {password}")
		print("*"*85)
	elif short_code == "li":
		print("*"*50)
		print("Enter your User Name your Password to log in:")
		print('*' * 50)
		username = input("User name: ")
		password = input("password: ")
		login = login_user(username, password)
		if login_user == "cc":
			print(f"Hello {username}. Welcome To Password Locker Manager")
			print('\n')

	while True:
		print("Use these short codes:\n CC - Create a new credentials  \n DC - Display Credentials  \n FC - Find a Credential \n GP -Generate a random Password \n D - Delete Credentials \n EX - Exit the application \n")
		short_code = input().lower().strip()
		if short_code == "cc":
			print("Create New Credentials")
			print("."*20)
			print("Account name ...")
			account = input().lower()
			print("Your Account username")
			username = input()
			while True:
				print(" TP - Type Password if you already have an account: \n GP - Generate random Password")
				if password_Choice == 'tp':
					password = input("Enter Your Password \n")
					break
				elif Password_Choice == 'gp':
					password = generate_password()
					break
				else:
					print("Invalid Password.Please try again")

			save_credentials(create_new_credentials(account, userName, password))
			print('\n')
			print(f"Account Credentials for: {account} - userName: {userName} - password: {password} successfully created")
			print('\n')
		elif short_code == "dc":
			if display_accounts_details():
				print("Here's your list of accounts:")

				print('*' * 30)
				print('_' * 30)
				for account in display_accounts_details():
					print(f" Account:{account.account} \n UserName:{username} \n Password:{password}")
					print('_'* 30)
				print('*' * 30)
			else:
				print("You don't have any credentials saved yet ...")
		elif short_code == "fc":
			print("Enter the account name of the Credentials you want to delete")
			search_name = input().lower()
			if find_credentials(search_name):
				search_credentials = find_credentials(search_name)
				print(f"Account Name : {search_credentials.account}")
				print('-' * 50)
				print(f"User Name: {search_credentials.username} Password: {search_credentials.password}")
				print('-' * 50)
			else:
				print("That Credential does not exist")
				print('\n')
		elif short_code == "d":
			print("Enter the Account Name you want to delete")
			search_name = input().lower()
			if find_credentials(search_name):
				search_credentials = find_credentials(search_name)
				print("_"*50)
				search_credentials.delete_credentials()
				print('\n')
				print(f"Your stored credentials for: {search_credentials.account} successfully deleted!!!")
				print('\n')
			else:
				print("That Credential you want to delete does not exist in your store yet")

		elif short_code == 'gp':
			password = generate_password()
			print(f" {password} Has been generated successfully. Please proceed into your account")
		
		elif short_code == 'ex':
			print(f"Thank You For Choosing D-Password Locker. See you next time")
			break
		else:
			print("Wrong entry! Check your entry again and let it match those in the Menu")

	else:
		print("Please enter a valid input to continue")

if __name__ == '__main__':
	   password()