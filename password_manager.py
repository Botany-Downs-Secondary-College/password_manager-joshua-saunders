#password_manager.py
#programme that allows the user to store and view passwords
#Joshua Saunders 23/02/2021

#variables
name = ""
age = ""
#empty password list 
password_list = []

#list for existing members and store new username
member_list = ["Wongster", "MokoMan115"]


#Functions  prints out the menu for the user to choose an option and returns user option to the main routine
def menu(name, age):

  print("Hello ", name)
  
  if age < 13:
    print("Sorry you do not qualified to enter")
    exit()

  else:
    mode = input("""Choose a mode by entering the number: 
    1: Add Passwords 2: View Passwords 3: Exit: """).strip()
    return mode 

#main routine

print("Welcome to the Password Manager")

name = input("What is your name")
age = int(input("How old are you?"))

menu()
def add details():
while True:
  #asks the user input and .upper converts the users input to upper case
  member = input("Enter | L for log in or | N to create a new account: ")

  if member == "L":
    m_username = input("Enter Username: ")
    m_password = input("Enter Password: ")
    if m_username and m_password in member list:
      print("Log In Successful")
      break
  elif member == "N":
    m_username = input("Enter username: ")
    m_password = input("Create Password with at least 8 characters long, Enter Password: ").strip()
    
    member_list.append(m_username, m_password)
    print("Your account created ")

def view_list ():
  print(member_list)

while True:
  chosen_option = menu(name, age)

  if chosen_option == "1":
    add_details()

  elif chosen_option == "2":
    view_list()

  elif chosen_option == "3":
    break
  
  else:
    print("That was no a valid optoin, please try again")

print("Goodbye, thanks for using password manager")