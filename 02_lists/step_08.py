MAX_LENGTH = 3



def shorten(lst):
    while len(lst) > MAX_LENGTH:
        remove_item = lst.pop()
        print(remove_item)
        
        
def get_list():
    lst = []
    element = input("Enter an element (or press Enter to stop): ")
    while element != "":
        lst.append(element)
        element = input("Enter an element (or press Enter to stop): ")
    return lst

def main():
    lst = get_list()  # User se list lo
    shorten(lst)  # List ko short karo

main()

    