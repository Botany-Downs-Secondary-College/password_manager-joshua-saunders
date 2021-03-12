#password_manager.py
#
print("Hi, welcome to Eugene's password programme. You must be 13 or over to qualify. ")

password_list = []
user_list = []



#Functions 

def age():
  while True:
    try:
      age = int(float(input("What is your age: ")))
      if age < 13:
        print("You do not qualify")
        exit()
      elif age >= 13:
        print("You qualify and may proceed.")
        break
    except IndexError:
        print("Enter correct index")
    except ValueError:
        print("Enter a integer not a word")
    except NameError:
        print("Please enter valid variable")
age()
      

def login():
  while True:
    user = input("are you a existing user? yes/no ")
    if user == "yes":
      username = input("Username: ")
    elif user == "no":
      print(option)
    elif username in user_list:
      password = input("Password: ")
    elif password in password_list:
      break
    else: 
        print("User was not in list please try again")


def new_user():
  while True:

    new_user = input("Enter a username to create a user for a new account: ")
    x = len(new_user)
    print(x)
    if x >= 5:
      print("Amount of letters in username qualify")
      user_list.append(new_user)
      break
    else:
      print("Username is too short must contain 5 or more letters")

def password():
    while True:
        new_password = input("Please enter a password (must be 8 or higher): ")
        y = len(new_password)
        print(y, "is the amount of letters in your pass")
        if y >= 8:
            print("password length qualify")
            password_list.append(new_password)
            break
        else:
            print("Password is too short try again."
