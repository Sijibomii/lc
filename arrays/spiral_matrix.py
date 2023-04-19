# keep row and column data to know the row i'm done with
# [l,d,r,u] continue going in the right direction until you reach an edge or an element that has been considered
# [[1,2,3],[4,5,6],[7,8,9]] 
# we do it for the first n * m matrix when we are don we do the same for the inner (n-2)*(m-2) matrix
# for each direction add the first n-1 entries in the matrix


def spiralOrder(self, matrix):
    res = []
    if len(matrix) == 0:
        return res
    
    row_begin = 0
    col_begin = 0
    # the number of columns equals the row_end. the col determines where a row ends
    row_end = len(matrix)-1 
    # the nu
    col_end = len(matrix[0])-1
    while (row_begin <= row_end and col_begin <= col_end):
        # left direction
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        # move row begin to next row incr row begin bc the next left should happen at the next row(below the forst row)
        row_begin += 1
        # down direction
        for i in range(row_begin,row_end+1):
            res.append(matrix[i][col_end])
        # reduce the col end here bc the next down should happen at the second to the last col
        col_end -= 1 
        if (row_begin <= row_end):
            # right direction. the if statement is needed bc only when the condition is valid is a right drn posible.
            # row_begin > row_end is a problem
            for i in range(col_end,col_begin-1,-1):
                res.append(matrix[row_end][i])
            # reduce the row end bc the next right should happen at the second to the last row
            row_end -= 1
        if (col_begin <= col_end):
            # up direction
            for i in range(row_end,row_begin-1,-1):
                res.append(matrix[i][col_begin])
            # move begin to next col
            col_begin += 1
    return res




"""
works for square matrix only
"""
def spiral_matrix(square_matrix):
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square-matrix has odd dimension, and we are at the center of the matrix square_matrix
            spiral_ordering.append(square_matrix[offset][offset])
            return
        # unpack each layer
        #https://www.programiz.com/python-programming/methods/list/extend
        # first move in the left dirn but leave out the edge bc next drn will start at the edge
        spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
        # next move in the down direction once again it leaves out the edge
        spiral_ordering.extend(list(
            #https://www.w3schools.com/python/ref_func_zip.asp
            #Unpacked argument lists: Given a sequence of arguments args, f(*args) will call f such that each element in args is a separate positional argument of f
            zip(*square_matrix))[-1-offset][offset:-1-offset])
        # next move in the right dirn once again leave out the edge
        spiral_ordering.extend(square_matrix[-1 - offset] [-1-offset:offset:-1])
        # next move in the up dirn once again leave out the edge
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1-offset:offset:-1]
            )
    spiral_ordering = []
    # for offset in range((len(square_matrix) + 1) // 2)-> this gives the number of layers the matrix has 
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering


