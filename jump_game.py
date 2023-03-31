# https://leetcode.com/problems/jump-game-ii/solutions/1192401/easy-solutions-w-explanation-optimizations-from-brute-force-to-dp-to-greedy-bfs/
# brute force algo
def jump_game(nums, curr=0):
    if curr >= len(nums) - 1:
        # recursion stopping condition
        return 0

    minJumps = float('inf')
    j=1
    while j<= nums[curr]:
        # this tries all the possible jumps at each step
        # when at 2 if first tries to go through the array with an initial jump of 1, then tries 2 also and computes the min
        # at each point in the array try all possible steps from where you are till the end
        # the reason there is a 1 here '1+jump_game(nums, curr + j)' is bc look at the smallest input type say: [2,3]
        # the stopping condiftion when nums[curr] = 3 returns 0, min of anything and 0 always returns 0 and since while loop runs of j <= nums[curr] and j starts at 0
        # a situation where we have a 0 num is covered. note stopping condition only returns 0 when curr has at least reach the last arr item
        """
        special case when nums = [2,1,0,3]. this is not solvable when curr = 2 the while loop will not run so it returns float('inf') to the caller func. the caller 
        func also has float('inf') as minJump so float('inf') get returned back up to the first calling func
        """
        minJumps = min(minJumps, 1+jump_game(nums, curr + j))
        j = j + 1
    return minJumps

print(jump_game([2,3,1,1,4])) 

### dynamic programming soln
"""
the idea behind dynamic programming is caching some of the results. instead of calculating the same result in a loop like above we cache the smallest jump 
from each point and just use it when needed
"""

def jump(nums):
    dp = [float('inf')]*len(nums)
    return solver(nums, dp, 0)

def solver(nums, dp, pos):
    if pos >= len(nums) - 1:
        return 0
    
    if dp[pos] != float('inf'):
        # return previously calculated value. it means the shortest jump from this position to the end has been prev calc.
        return dp[pos]
    j = 1
    while j <= nums[pos]:
        dp[pos] = min(dp[pos], 1+solver(nums, dp, pos +j))
        j=j+1
    return dp[pos]

print(jump([2,3,1,1,4])) 