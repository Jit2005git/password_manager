import random
import string
passwords={}
#load existing passwords from file
try:
    with open("passwords.txt", "r") as file:
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
    print("1.  Save password ")
    print("2. View existing passwords")
    print("3.Generate a new password")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        site=input("Enter the website name: ")
        pwd=input("Enter the password: ")
        passwords[site]=pwd
        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
            print("Password saved successfully!")
    elif choice=="2":
        if not passwords:
            print("No passwords saved yet.")
        else:
            for site, pwd in passwords.items():
                print(f"{site}: {pwd}") 
    elif choice=="3":
        new_pwd=generate_password()
        print(f"Generated password: {new_pwd}")
    elif choice=="4":
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

