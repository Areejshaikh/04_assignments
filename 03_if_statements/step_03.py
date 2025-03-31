def leap_year():
    user_input = int(input("Enter Your  Number! "))
    
    if(user_input % 4 == 0):
        if(user_input % 100 == 0):
            if(user_input % 400 == 0 ):
                print("That' leap year! ")
            else:
                print("That's not a leap year.")
        else:  # (Not divisible by 100)
            print("That's a leap year!")
    else:  # (Not divisible by 4)
        print("That's not a leap year.")
leap_year() 