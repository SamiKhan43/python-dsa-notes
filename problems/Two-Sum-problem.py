"""
Given a list of integers nums and an integer target
return True if two different elements add up to target,
otherwise False.

Constraints: n can be up to 100,000.

nums = [2, 7, 11, 15], target = 9   →  True
nums = [1, 2, 3], target = 10       →  False
nums = [3, 3], target = 6           →  True
"""

def bruteforce_find_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True

    return False
    #time comp : o(n^2)
    #space comp : 0(1)

def set_find_sum(nums , target):
    seen = set()
    for num in nums:
        required = target - num  
        if required in seen:
            return True
            seen.add(num)

    return False

    #time comp : o(n)
    #space comp : 0(n)

