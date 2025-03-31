import random


dic_sides = 6

def dic():
    dic1 : int= random.randint(1 , dic_sides )
    dic2 : int = random.randint(1, dic_sides)
    dic_Total = dic1 + dic2
    print(f"dis One is: {dic1} and dis two is : {dic2} =  {dic_Total}")
    
    
    
    # Loop for print 3 time dics
for i in  range(3):
    print (f"Roll {i+ 1}")
    dic()
    print()
    

    