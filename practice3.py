def remove_negatove(nums):
    positive_nums = []
    for num in nums:
        if num >= 0:
            positive_nums.append(num)
    return positive_nums
nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive_numbers = remove_negatove(nums)
print(f"Positive numbers: {positive_numbers}")