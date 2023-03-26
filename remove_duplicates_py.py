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
       