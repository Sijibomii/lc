# this prob can be solved with dynamic prog. the technique of dp is to find the soln to the smallest problem and from that solution, find the solution to the next 
# smallest soln. i.e the soln just bigger than the smallest. this is the BOTTOM TOP APPROACH
# https://www.youtube.com/watch?v=Q6rwr41Hml8
def unique_path(m, n):
    lower=[1]*n
    for i in reversed(range(m-1)):
        upper= [0]*n
        upper[n-1] = 1
        for j in reversed(range(n-1)):
            upper[j] = upper[j+1] + lower[j]
        lower = upper
    return lower[0]

# recursive dp soln. 
def unique_path(m, n):
    @cache
    def dp(i, j):
        if i== m-1 or j == n-1:
            return 1
        return dp(i+1,j)+ dp(i, j+1)
    return dp(0,0)
    


"""
permutation and combination method. since we are starting from (0,0) to (m-1, n-1) there are a total of T=(m-1)+(n-1) steps needed. and out of that T(total) steps, a 
(m-1) has to be in the right direction and (n-1) in the down drn. to find all possible soln, its the same as "picking" (m-1) Right from T steps or "picking"
(n-1) down drn from T steps. 
For permutation: ORDER MATTERS and each obj is distinct
For combination: ORDER DOES not matter.
Here, there are just 2 directions a R and D. ALL Rs are equal, same with D. You just have to pick two slots for D. Just like Red balls. Two red balls are the same
they are not distinct. this is combination
VIDEO EXPLAINING THE DIFF -> https://www.youtube.com/watch?v=3S8hs6aEts0
i.e if a set of options or objects are not distinct from the other and are "equal" comb is used. just like here, every R is "equal" to other R and every D is
equal to D
"""
import math
def unique_path(m, n):
    # combination. can be TC(m-1)(m-1 Ds) or TC(n-1) (n-1 Ds). T= m-1+n-1 or m+n-2
    math.comb(m+n+2, m-1)
