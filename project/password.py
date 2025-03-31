import random
print("Welcome To Your Password Generator ")
chars = ("qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%^&*")
number = input("Amount to Password generate: ")
number = int(number)
length = input("Enter Password Length: ")
length = int(length)

print("\n here are Your Password:")

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)