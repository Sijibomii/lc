# brute force algo
"""
brute force algo consideres all sub arrays and return max
"""
def maxSubArray(nums):
    ans = float('-inf')
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            ans = max(ans, cur_sum)
    return ans

#recursive brute force algo
def maxSubArray(nums):
    def solve(i, must_pick):
        if i >= len(nums): return 0 if must_pick else float('-inf')
        return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
    return solve(0, False)


# loop through the arr. if total sum drops to -ve switch starting pos
# [-2,1,-3,4,-1,2,1,-7,4] -> [4,-1,2,1]
def maximum_subarray(nums):
    max_sum = 0
    curr_sum, curr_start = 0,0
    starting_idx, ending_idx = 0, len(nums)-1
    for i in range(len(nums)):
        curr_sum = curr_sum + nums[i] #-2
        
        if curr_sum < 0:
            curr_sum = 0
            curr_start = i+1
            # assuming there will always be a max subarray before we get to the end


        if curr_sum > max_sum:
            max_sum = curr_sum
            starting_idx = curr_start
            ending_idx = i + 1
    """
    uncomment this if you are returning the array and not just the max sum
    """
    # if ending_idx > len(nums) - 1:
    #     return nums[starting_idx:]   
    # return nums[starting_idx: ending_idx]
    return max_sum

print(maximum_subarray([5,4,-1,7,8]))

# https://www.youtube.com/watch?v=yPTghcz7OME
# [-2,1,-3,4,-1,2,1,-7,4] -> [4,-1,2,1]
"""
since we are after the max number alone we pick the one with maximum res always
for the array above, res= -ve inf, prev_end stores the max btw the curr number and the curr_sum kind off.
if the current sum goes below curr number then that curr can not be the maximum subarray. res holds the max_sum
"""
def maxSubArray(nums):
    res = float('-inf')
    prev_end = 0
    for n in nums:
        prev_end = max(n, prev_end+n)
        res = max(res, prev_end)
    return res

# https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/
# recursive
# [-2,1,-3,4,-1,2,1,-7,4] -> [4,-1,2,1]
"""
This solution is the recursive version of the brute force algo. it considers all subarrays in the array.
For every element in the array, we can choose to "pick" this current element to be included in the subarray or not.

If we had picked any elements till now, we can either end further recursion at any time by returning sum formed till now or we can choose 
current element and recurse further. This denotes two choices of either choosing the subarray formed from 1st picked element till now or 
expanding the subarray by choosing current element respectively.
"""
def maxSubArrayy(nums):
    def solve(i, must_pick):
        # this condition is when i > len(nums) i.e there's an overflow
        if i >= len(nums): return 0 if must_pick else float('-inf')
        """
        at each element when choosing our subarray, we have an option to not include or include the element is the subarray being considered
        the line below finds the maximum sum out of the two consideration using recursion. It calculates the sum when the number is included
        and when its not and finds the maximum.
        """
        return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
    return solve(0, False)
  
print(maxSubArrayy([-2,1,-3,4,-1,2,1,-7,4]))    

#dynamic programming
"""
this solution is just the same as above but the diff is after the max of a sub array is calc, it is stored in dp
i.e to calc th sum of [-2,1,-3,4] you just need to calc [-2,1,-3] and add 4. if this([-2,1,-3]) has been cached you do not need to recalculate it
"""
def maxSubArray(nums):#[[0,0,][]]
    dp = [[0]*len(nums) for i in range(2)]
    dp[0][0], dp[1][0] = nums[0], nums[0]
    for i in range(1, len(nums)):
        dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
        dp[0][i] = max(dp[0][i-1], dp[1][i])
    return dp[0][-1]

# kadene's algo
def maxSubArray(nums):
    cur_max, max_till_now = 0, float('-inf')
    for c in nums:
        cur_max = max(c, cur_max + c)
        max_till_now = max(max_till_now, cur_max)
    return max_till_now

# divide and conquer
def maxSubArray(nums):
    def maxSubArray(A, L, R):
        if L > R: return float('-inf')
        mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
        for i in range(mid-1, L-1, -1):
            left_sum = max(left_sum, cur_sum := cur_sum + A[i])
        cur_sum = 0
        for i in range(mid+1, R+1):
            right_sum = max(right_sum, cur_sum := cur_sum + A[i])
        return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
    return maxSubArray(nums, 0, len(nums)-1) 
