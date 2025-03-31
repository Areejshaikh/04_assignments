import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
  for MIN_VALUE in range(N_NUMBERS):
     random_number = random.randint(MIN_VALUE ,MAX_VALUE)
     print(random_number , " ")
     

if __name__ == '__main__':
    main()
