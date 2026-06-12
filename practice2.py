def find_largest(number):
    largest_num = 0
    for num in number:
        if num > largest_num:
            largest_num = num
    return largest_num
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = find_largest(num)
print(f"The largest number is: {largest}")