
# [1,0,-1,0,-2,2] target = 0
def four_sum(nums, target):
    # pick one value and run the remaining part of the list as a three sum 
    answer = set()
    for idx, num in enumerate(nums):
        answer |= three_sum(nums[idx:], target - num, num)
    new_ans = set()
    for li in list(answer):
        new_ans.add(tuple(sorted(list(li))))
    return list(new_ans)
def three_sum(nums, target, number):
    nums = sorted(nums)

    answer = set()
    for idx, num in enumerate(nums):
        low = idx + 1
        high = len(nums) - 1
        while low < high:
            if num + nums[low] + nums[high] < target:
                #increment low to find an higher number so total can move closer to 0
                low = low + 1
            elif num + nums[low] + nums[high] > target:
                #increment hight to find a lower number so the total can move closer to 0
                high = high - 1
            else:
                # a match has been found i.e total = target
                answer.add((num, nums[low], nums[high], number))
                # logic below is meant to eliminate duplicates to save time
                temp1 = low
                temp2 = high
                while (low < high) and (nums[low] == nums[temp1]):
                    #[-1, 0,1,1,1,3,4,5] assuming low was at index 2, we skip new low to index 5 since others are duplicates
                    low= low + 1
                while (low < high) and (nums[high] == nums[temp2]):
                    #same logic but for high
                    high = high - 1
    return answer



"""
Alternative sol
"""

def fourSum(nums, target):
    n = len(nums)
    seen = set()
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                lastNumber = target - nums[i] - nums[j] - nums[k]
                if lastNumber in seen:
                    arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                    ans.add((arr[0], arr[1], arr[2], arr[3]))
        seen.add(nums[i])
    return ans