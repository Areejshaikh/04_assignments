def main():
    
    for i in range(10):
        if is_odd(i):
            
            print("ODD")
        else:
            print("Even")
            
def is_odd(value : int):
     remainder = value  % 2
     return remainder == 1
 
 
 
main()
        