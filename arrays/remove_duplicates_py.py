def remove_dup(nums):
    i,j=0,1
    while i<=j and j<len(nums):
        if nums[i]==nums[j]:
            j+=1
        else:
            nums[i+1]=nums[j]
            i+=1
    return i+1

print(remove_dup([0,0,1,1,1,2,2,3,3,4]))


def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return A[:write_index]

print(delete_duplicates([0,0,1,1,1,2,2,3,3,4]))