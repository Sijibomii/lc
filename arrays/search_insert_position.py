
# binary search
# find middle, if middle > target left = mid + 1 else right = mid - 1
"""
Input: nums = [1,3,5,6,7], target = 2
Output: 1
https://leetcode.com/problems/search-insert-position/solutions/249092/come-on-forget-the-binary-search-pattern-template-try-understand-it/
"""
def search_insert(nums, target):
    left, right = 0, len(nums) -1
    
    while left < right:
        mid = int((left+right)/2)

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            # insertion point could be in at least m + 1, since nums[m] < target
            left = mid + 1
        else:
            # insertion point could be in at least m, since nums[m] > target. if nums[m] is only num > target, insertion point will be m. so it should be m not m -1
            right = mid 

    # at this point l=m=r. the stopping condition for our loop is l<r so when there's just one more el in consideration space loop terminates
    # check if nums[left] < target if so, return left+1 else left
    return  left+1 if nums[left] < target else left 


print(search_insert([1,3,5,6], 2))

    