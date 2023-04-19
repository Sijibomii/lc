# https://leetcode.com/problems/rotate-image/solutions/1449737/rotation-90-code-180-270-360-explanation-inplace-o-1-space/

def rotate_image(matrix):
    n = len(matrix)
    """
    check link above for pictorial explaination
    """
    # this finds the transpose of the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # swap colums. 1.e first and last, second and second to the last .....
    for i in range(n):
        left, right = 0, n-1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left = left + 1
            right = right - 1
    return matrix

print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))

# https://www.youtube.com/watch?v=fMSJSS7eO1w
def rotate(a):
    """
    Do not return anything, modify matrix in-place instead.
    """
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
