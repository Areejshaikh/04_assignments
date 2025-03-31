def averages (num1:float , num2:float):
    total_averages = num1 + num2 / 2
    return total_averages


def main ():
    
    
    arvg1 = averages(1,3)
    arvg2 = averages(1,5)
    
    final_average = averages(arvg1 , arvg2)
    
    print(final_average)
main()


