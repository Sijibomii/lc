"""
    No rotated:
    1 2 3 4 5 6 7

            
    left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
    3 4 5 6 7 1 2 , mid => 6 . mid is part of the rotated elements

    search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

    right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
    6 7 1 2 3 4 5, mid = 2. mid is not part of the rotated elements
          
    search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
"""

"""
basically since the array is rotated, one part should at least be in correct ascending order, find that part and check if target is within that range,
if not go to the other part and start over. i.e find the part(in the second part that is in correct ascending order) and cont...

"""

def search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if target == nums[int(mid)]:
            return int(mid)

        if nums[int(low)] <= nums[int(mid)]:
            # mid is part of the rotated elements. since mid is part of the rotated elements, low...mid is in asc order
            if nums[int(low)] <= target <= nums[int(mid)]:
                # target is between low and mid. continue binary search on left part
                high = mid - 1
            else:
                 # target should be between mid and high. re start operation on the right side. get new mid, 
                low = mid + 1 
        else:
            # mid is not part of the rotated elements
            if nums[int(mid)] <= target <= nums[int(high)]:
                # target should be between mid and high
                low = mid + 1
            else:
                # target should be between low and mid
                high = mid - 1

    return -1

print(search([4,5,6,7,8,2,3],8))
