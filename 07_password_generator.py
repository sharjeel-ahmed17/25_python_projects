import random 

print("Welcome to the Password Generator!")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
number = int(input("How many passwords do you want to generate? "))
length = int(input("How long do you want your passwords to be? "))
passwords = []
for _ in range(number):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    passwords.append(password)
print("Here are your passwords:")
for password in passwords:
    print(password)

