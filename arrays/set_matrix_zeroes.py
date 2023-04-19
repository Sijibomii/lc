
def set_matrix_zeroes(matrix):
    # boolean to track if a zero has been seen on the first row and col resp
    isZeroCol = False
    isZeroRow = False
    for i in range(len(matrix)):
        # check the first column for any zero element
        if matrix[i][0] == 0:
            isZeroCol = True
            break
    
    for i in range(len(matrix[0])):
        # check the first row for any zero element
        if matrix[0][i] == 0:
            isZeroRow = True
            break
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            # check all other elements if any element is seen as a Zero set the "parent" i.e top col - first element on that col 
            # and top row - first element on that row to zero. this helps us determine which cols and rows will be set to 0
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
            
    """
    now, process all columns and row i.e if top col or top row equals zero set all elements on that row and col resp to zero
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                # this elements top col or top row equals zero
                matrix[i][j] = 0

    if isZeroCol:
        # process first column. in the loop above the loop starts from row and col 1 top prevent tampering with first col and row used within the loop
        for i in range(len(matrix)):
            # isZeroCol meanings the first col shoul be set to zero
            matrix[i][0] = 0

    if isZeroRow:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0