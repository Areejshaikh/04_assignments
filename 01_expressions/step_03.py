feet_per_inch: float = 12

def feet_convert_inches():
    user_input = float(input("enter number of Feet! "))
    total_inches = user_input * feet_per_inch
    
    
    print (f"That is {total_inches} Inches! ")
feet_convert_inches()