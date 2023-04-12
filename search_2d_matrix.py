# it is basically an advanced version of the binary search
"""
the whole matrix is treated as a list and a binary search is used to find target
"""
def serch_2d_matrix(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    
    while low <= high:
        mid = (low + high) / 2
        # the formular to get row and col is based on the way the element counting works. Elements are counted row by row, that's why thay 
        # formular work.
        num = matrix[int(mid / cols)][mid % cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False
    