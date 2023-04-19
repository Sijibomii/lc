
### MY SOLUTION
def three_sum_closest(nums, target):
    nums = sorted(nums)
    diff = [float('inf'), float('inf')] # [absolute_diff, sum]
    for idx, num in enumerate(nums):
        low = idx + 1
        high = len(nums) -1
        while low < high:
            if num + nums[low] + nums[high] < target:
                curr_diff = target - (num + nums[low] + nums[high])
                if abs(curr_diff) < diff[0]:
                    diff = [abs(curr_diff), num + nums[low] + nums[high]]
                
                low = low + 1
            elif num + nums[low] + nums[high] > target:
                curr_diff = (num + nums[low] + nums[high]) - target 
                if abs(curr_diff) < diff[0]:
                    diff = [abs(curr_diff), num + nums[low] + nums[high]]
                high = high - 1
            else:
                #since target matched
                return num + nums[low] + nums[high]
    return diff[1]