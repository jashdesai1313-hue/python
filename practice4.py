def create_and_sum_list():
    numbers = [] 
    while True:
        num = float(input("Enter a number (0 to stop): "))      
        if num == 0:
            break  
        numbers.append(num)
    return sum(numbers)