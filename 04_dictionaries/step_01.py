def read_phone_book():
    
    phoneBook = {}
    
    while True:
        name = input("Name: ")
        if (name == ""):
            break
        number = input("number: ")
        phoneBook[name] = number
        
        return phoneBook
 


def print_phoneBook(phoneBook):
    
    for name in phoneBook:
        print(f"{name} -> {phoneBook[name]}" )
        
        
        
        
def lookup_number(phoneBook):
    
    
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if (name not in phoneBook):
             print(name + " is not in the phonebook: ")
        else:
             print(phoneBook[name])
             
             
def main ():
    phoneBook = read_phone_book()
    print_phoneBook(phoneBook)
    lookup_number(phoneBook)
    
    
    
    
main()
        


    
    
    
    