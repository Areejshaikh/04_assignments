def print_digits(num):
    once_digits = num % 10
    print(f"The once digits is {once_digits}")
    
    
def main():
    num = int(input("Enter a number: "))
    print_digits(num)
main()