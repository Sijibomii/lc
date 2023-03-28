"""
perform two binary searches the first one (searchleft), moves the left cursor graudually until it finds the first left. it keeps moving right backwards, for each time of 
the iteration where target is <= mid. once it finds a mid point that is > target it shifts left pointer forward.

reverse is the case for right
"""

# Input: nums = [5,7,7,7 ,7,8,8,10,11], target = 7 Output: [3,4]
def find_first_and_last(nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]