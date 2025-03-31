adult_age = 18 


def main(age : int):
    
    if (age >= adult_age):
        return True
    else:
        return False
    
    
def persons_age():
    age: str = int(input("How old is this person?: "))
    print(main(age))
    
    
    
persons_age()