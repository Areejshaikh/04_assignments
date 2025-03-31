def fruitsShop():
    fruits = {
         "apple " : 1.5, 
         "kiwi" : 50, 
         "Mongo" : 80,
         "peach" : 1.5, 
         "Struberry" : 1,
         "graps" : 7
         }
    
    total_cost = 0
    
    for fruits_name in fruits:
        price = fruits[fruits_name]
        amount_bought = int(input("How Many (" + fruits_name+") do you want to buy?: "))
        total_cost += (price * amount_bought)
        
    print(f"Your total is $ {total_cost}")
        
        
fruitsShop()