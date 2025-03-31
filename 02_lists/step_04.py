def add_three_copies(my_list, data):
    for  i in range(6):
        my_list.append(data)
        
def main ():
    message = input("Enter a message today? ")
    my_list = []
    print(f"List Before {my_list}")
    
    add_three_copies(my_list, message)
    print(f"List after {my_list}")
main()