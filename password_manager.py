#password_manager.py
#Joshua Saunders 25/02/2021

#Lists
password_list = ["Pass1234"]
username_list = ["BDSC2021"]


#Functions
def line():
  print("     ")

def age():
  while True:
    try:
      age = int(float(input("What is you age: ")))
      
      if age < 13: 
        print("Sorry you are not old enough")
        break
      elif age >= 13:
        print("Hello {}".format(name))
        menu()
        break
    except ValueError:
      print("Enter an integer not a word please")


def menu():
  while True:
    try:
     options = int(input("1: New User | 2: Existing User | 3: View Username List | 4: View Passwords List | 5: Exit: "))
     if options == 1:
       line()
       add_user()
     elif options == 2:
       log_in()
     elif options == 3:
       print(username_list)
       menu()
     elif options == 4:
       print(password_list)
       menu()
    
     elif options == 5:
       break
     else:
      print("Please enter a number from the ones shown")
    except ValueError:
     print("Enter a number shown from the options given")

def add_user():
  while True:
    add_username = input(("Enter a username to create a user for a new account: "))
    x = len(add_username)
    if x >= 10:
      print("Username is created")
      username_list.append(add_username)
      password()
    else:
      print("Username is too short, it must contain 5 or more letters")

def password():
  while True:
    add_password = input("Please enter a password, must be 8 letters or more: ")
    y = len(add_password)
    if y >= 8:
      print("Password length is sufficent")
      password_list.append(add_password)
      menu()
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
    if add_extra == 1:
      print(username_list)
      print(password_list)
      break
    if add_extra == 2:
      add_user()
      password()
    else:
      print("User was not found please try again")


name = input("What is you name: ")
age()
