def main():
    numbers = [1,2,3,4,5]
    for i in range(len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 4 
    print(numbers)
main()
    