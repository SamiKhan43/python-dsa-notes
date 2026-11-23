""" 
Count Increases
Problem
Count how many numbers are bigger than the number directly before them.

[5, 3, 4] -> 1 (only 3 -> 4)
[1, 2, 3] -> 2 (1 -> 2, 2 -> 3)

## Edge cases
[]` -> 0
[7]` -> 0 (the first item has nothing before it)

"""


def count_increases(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
            
    return count

#Time: O(n), one pass through the list
#Space: O(1), only count 

