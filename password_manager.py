import random
import string
passwords={}
#load existing passwords from file
try:
    with open("passwords.txt", "r") as file
        for line in file:
            website,pwd = line.strip().split(":")
            passwords[website] = pwd
except :
    pass
def generate_password():
    chars=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(chars) for i in range(8))
    return password
while True:
    print("\n ------ Password Manager ------")
    print("1. Generate a new password")
    print("2. View existing passwords")
    print("3. Save password")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
