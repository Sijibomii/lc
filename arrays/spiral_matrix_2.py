# https://leetcode.com/problems/spiral-matrix-ii/solutions/22282/4-9-lines-python-solutions/

"""
Start with the empty matrix, add the numbers in reverse order until we added the number
always rotate the array and add new elements to fill the top row
1. insert 9 first. [9] -> one row and one col. rotating this and add the next el in reverse order to the top row -> |8|
                                                                                                                    |9|
next rotate again to [9,8] and insert 6,7 to top row... continue that way                                                                                                           
"""
def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
