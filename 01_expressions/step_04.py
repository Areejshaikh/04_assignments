import math



def main():
    
    ab =  float(input("enter your Number AB: "))
    ac =  float(input("enter your Number AC: ")) 
    bc: float= math.sqrt(ab**2 + ac**2)
    
    print(f"The length of BC (the hypotenuse) is: {bc}")
main()