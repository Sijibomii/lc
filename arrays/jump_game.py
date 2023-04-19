# dp algo for solving result will return -inf if it could not reach the end bc -inf will always be less
def jump_game(nums):
    res = float('inf')
    dp=[float('inf')]*len(nums)

    def solver(nums, dp, position):
        print("mm")
        if position >= len(nums) -1:
            return 0
        
        if dp[position] != float('inf'):
            return dp[position]

        j = 1
        while j <= nums[position]:
            """
            [2,3] dp=[inf,inf]. obviously by if statement above we avoid returning -inf 
            we start with 1 jump at first min(inf, 1) which is 1continues on
            """
            dp[position] = min(dp[position], 1+solver(nums, dp, position +j))
            j=j+1
        return dp[position]
    
    res = solver(nums, dp, 0)
    return False if res == float('inf') else True

print(jump_game([2,3]))

## algo 2
def canJump(nums):
    last_position = len(nums)-1

    # start from the len(nums)-2, to -1 i.e it list numbers in decr order from len(nums)-2 to 0
    for i in range(len(nums)-2,-1,-1): 
        if (i + nums[i]) >= last_position: 
            # meaning we can get from second to last position to last position
            last_position = i 
    return last_position == 0	