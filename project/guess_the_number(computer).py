import random

# Create function
def guess (x):
  random_number = random.randint(1 , x)
  guess = 0


  # Logic
  while guess != random_number:
    guess = int(input(f"Guess the  number between 1 and {x}: "))
    if guess < random_number:
      print(f"Sorry, guess Again, Too low: {guess}")
    elif guess > random_number:
      print(f"Sorry, guess Again, Too High: {guess}")


  print (f"Yes! you have guessed the correct  number {random_number}: " )

guess(10)



def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  # logic
  while feedback != 'c':
    if low != high:
      guess = random.randint(low , high)
    else:
      guess = low
  feedback = input(f"Is {guess} too high (H), too low (L), or correct (C) ?? ")
  if feedback == 'h':
    high = guess -1
  elif feedback == 'l':
     low = guess + 1
print (f'Yeh! The Computer guessed Your Number, correctly! ')
  # call function


computer_guess(5)