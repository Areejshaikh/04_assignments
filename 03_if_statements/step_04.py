average_tall = 50

def main():
    
    while True:
        user_input = input("How tall are you? ")
        
        if (user_input == ''):
            break
        height = float(user_input)
            
    
        if (height >= average_tall):
            print(f"You're tall enough to ride! {user_input}" )
        
        elif(height < average_tall):
            print("You're not tall enough to ride, but maybe next year!")
        break
main()