def main():
    curr_value = int(input("Enter your Number: "))
    double_value = int(input("Enter Your converted numbere! "))
    
    for curr_value in range(100):
        curr_value = curr_value * double_value
        print(curr_value)

main()