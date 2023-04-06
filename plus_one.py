
def plus_one(A):
    A[-1] += 1
    # [8,9] -> [8, 10] ->[0, 9]
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
    # There is a carry-out like in the case of 99, so we need one more digit to store the
    #result. A slick way to do this is to append a 0 at the 
    #end of the array,and       
    #update the first entry to 1.
        A[0] = 1
        A.append(0)
    return A

