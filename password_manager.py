#password_manager.py
#Joshua Saunders 25/02/2021

#Lists
password_list = ["Pass1234"]
username_list = ["BDSC2021"]


#Functions
def age():
  while True:
    try:
      age = int(float(input("What is you age: ")))
      
      if age < 10: 
        print("You are not old enough")
        break
      elif age >= 13:
        print("You are old enough please proceed")
        menu()
    except ValueError:
      print("Enter an integer not a word please: ")


def menu():
  while True:
    options = int(input("1: New User | 2: Existing User | 3: View Username List | 4: View Passwords List: "))
    if options == 1:
      add_user()
      password()
      break
    elif options == 2:
      log_in()
      break
    elif options == 3:
      print(username_list)
    elif options == 4:
      print(password_list)
      
      break
    else:
      print("Please enter a number to the ones shown")

def add_user():
  while True:

    add_user = ("Enter a username to create a user for a new account: ")
    x = len(add_user)
    if x >= 5:
      print("Username is created")
      username_list.append(add_user)
      break
    else:
      print("Username is too short, it must contain 5 or more letters")

def password():
  while True:
    add_password = input("Please enter a password, must be 8 letters or more: ")
    y = len(add_password)
    if y >= 10:
      print("Password length is sufficent")
      password_list.append(add_password)
      break
    else:
      print("Password is too short please enter one with 8 letters or more")
  
def log_in():
  while True:
    user = input("Are you an existing user? Yes/No: ").lower()
    if user == "yes":
      username = input("Username: ")
    elif user == "no":
      menu()
    if username in username_list:
      password = input("Password: ")
    if username not in username_list:
      print("Username not found, we have returned you back to the menu")
      menu()
    if password in password_list:
      add_extra = input("Welcome, Press 1 To View Your Lists, And Press 2 To Add More Passwords: ")
    elif add_extra == 1:
      print(username_list)
      print(password_list)
      break
    elif add_extra == 2:
      add_user()
      password()
    else:
      print("User was not found please try again")

age()
