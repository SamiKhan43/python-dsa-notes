"""
Contains Duplicate: 
Given a list of integers nums,
return True if any value appears at least twice,
and False if every element is distinct.

[1, 2, 3, 1]  →  True
[1, 2, 3, 4]  →  False
[]            →  False

"""

def contains_duplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
    #Time O(n^2), space O(1).


def contains_duplicate_set(nums):
    seen = set()
    for num in nums:
        if num in seen: 
            return True
        seen.add(num)   
    return False
    #Time O(n) on average, space O(n)

 
 
def contains_duplicate_shortcut(nums):
    return len(nums) != len(set(nums))   
     #Time O(n), space O(n). Cannot stop early.
