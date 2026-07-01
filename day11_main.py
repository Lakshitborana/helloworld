import day11_utils

nums = [int(x) for x in input("Enter numbers: ").split()]
print(nums)

print("Numbers:", nums)
print("Even numbers:", day11_utils.is_even(nums))
print("Maximum number:", day11_utils.find_max(nums))
print("Odd numbers:", day11_utils.is_odd(nums))