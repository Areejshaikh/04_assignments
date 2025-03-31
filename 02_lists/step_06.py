def get_element(first):
    print(first[0] -1)

def get_first_element():
    first = []
    element = input("Please enter an Element of The List: ")
    while element != "":
        first.append(element)
        element = input("Please enter an Element of The List: ")
    return first

def main():
    first = get_first_element()
    get_element(first)

main()