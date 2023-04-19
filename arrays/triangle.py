
# dp solution(bottom up soln)
"""
[[2],[3,4],[6,5,7],[4,1,8,3]]
the idea is to find the shortest distance from each "col".  At the bottom there are 4 cols(woild be always eq to no of rows). we start by initializing our dp
arr with those then we gradually move to the top. Starting from row[-2](since we're done with row[-1], see ##-1) every column in curr row (-2) we pretend like we've calc
the shortest path through that col in the current row and try to find the shorted path from there to the row below.

[6,5,7] -> we pretend like we've traced the shortest path from the root to col 0, (6) from here, we now cal shortest path from 6 to last row. We then find the min
distance btw 6 and its two children and store in col0, same for col 1 (5 and its two children) and col 2 (7 and its two children).

we move to the next row [3, 4]: min btw 3 and its two children(6,5) stored in col0, min btw 4 and its two children (5,7) stored in col1

"""
def triangle(triangle):
    # cache array
    dp = [0]*len(triangle)

    for i in range(len(triangle[-1])):##-1
        # the last row
        # fill the smallest part for each col as the bottom elements
        dp[i] = triangle[-1][i]

    for i in reversed(range(len(triangle)-1)):
        for j in range(i+1):
            # Find the lesser of its two children, and sum the current value in the triangle with it.
            dp[j] = min(dp[j], dp[j + 1])+ triangle[i][j]

    return dp[0]