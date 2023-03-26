

# MY SOLUNTION
def remove_elements(nums, target):
    i,j = 0,len(nums) -1
    # in place sorting is important
    nums.sort()
    # print(nums)
    while i < j:
        if nums[i] != target:
            # print(i)
            i = i+ 1
        else:
            nums[i] = nums[j]
            nums[j] = target
            i= i + 1
            j= j -1
    index = 0
    try:
        index = nums.index(target)
    except:
        index = len(nums)
    return index

   
"""
leetcode accepts this but it doesn't work on: remove_elements([3,2,2,3,4,5,3,3,3,4,5,3,6,3], 3)
"""

def remove_elements(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


# Input: nums = [0,1,2,2,3,0,4,2], val = 2
print(remove_elements([0,1,2,2,3,0,4,2], 2))
print(remove_elements([3,2,2,3,4,5,3,3,3,4,5,3,6,3], 3))
print(remove_elements([2], 3))
# [3,2,2,3]