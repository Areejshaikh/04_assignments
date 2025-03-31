def fruits_stock():
    fruit  = input("enter a fruits: ")
    stock = num_of_stock(fruit)
    if(stock == 0 ):
        print("This fruit is not in stock.")
        
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)
        
        
def num_of_stock(fruit):
    if(fruit == 'apple'):
        return 2
    if(fruit == 'peach'):
        return 4
    if(fruit == 'pear'):
        return 1000
    else:
	    return 0
 
 
fruits_stock()