def is_even(nums):
   print(type(nums))
   return nums % 2 == 0

def is_odd(nums):
   print(type(nums))
   return nums % 2 != 0

def find_max(nums):
    print(type(nums))
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
    