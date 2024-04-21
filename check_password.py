# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential Create a Python script to check the password strength. 
# ●       Implement a Python function called check_password_strength that takes a password string as input..
# ●       The function should check the password against the following criteria:
# ○       Minimum length: The password should be at least 8 characters long.
# ○       Contains both uppercase and lowercase letters.
# ○       Contains at least one digit (0-9).
# ○       Contains at least one special character (e.g., !, @, #, $, %).
# ●       The function should return a boolean value indicating whether the password meets the criteria.
# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
# ●       Provide appropriate feedback to the user based on the strength of the password.  
import re

def check_password_strength(password):
    if(len(password)<8): #password should be at least 8 characters 

        return False
    if not re.search(r'[A-Z]',password): #password should contain uppercase letters
        return False
    if not re.search(r'[a-z]',password): #password should contain lowercase letters
        return False
    if not re.search(r'\d',password): #password should contains digits
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password): #password should contain one special character
        return False  
    return True

userName = input("Enter your username: ")
password = input("Please enter the password: ")

value = check_password_strength(password)

if value:
    print("The password is strong")
else:
    print("""Password does not meet the requirements.
           Please ensure 
          1. The password is least 8 characters long 
          2. Contains both uppercase and lowercase letters
          3. Contains at least one digit (0-9)
          4. Contains at least one special character (e.g., !, @, #, $, %)""")