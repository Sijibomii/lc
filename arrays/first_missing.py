"""
this algo does not work for duplicates. Bug: say you have [2,2] as input, ans should be 1 
-> arr is padded with a 0 i.e [2,2,0].
-> first loop iter(second loop). nums[i]%n => 2%3 = 2 i.e nums[2] = nums[2] + n. [2,2,3] 
-> second loop iter(second loop). nums[i]%n => 2%3 = 2 i.e nums[2] = nums[2] + n. [2,2,6] 
-> issue with algo is the third loop which checks if a number nums[i]/n==0. i.e a position with 0 but the two's where left unchanged.
"""
def first_missing(nums):
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            # not len(n) has incr bc 0 was appended at start of func
            nums[i]=0
    print(nums)
    # nums[0] % 3 => 1 % 4 = 1, nums[1] = 6
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        # using this formular, the number of times 1 appears will be stored in the postion '1' of the array
        # the number of times two appears will be stored in postion '2' of the array. but we can still retrive the original value that was in each pos
        # since we just incr by n
        print(nums[i]%n) # 5
        nums[nums[i]%n] = nums[nums[i]%n] + n
    print(nums)
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            # meaning theres a position i that was not initially in the array
            return i
    return n
print(first_missing([2,2]))

#######################
def firstMissingPositive(nums):
    for i,num in enumerate(nums):
        if num <= 0:
            nums[i] = 0

    for i,num in enumerate(nums):
        index = abs(num)-1
        # the array itself is used as a flag. i.e if we've seen the number 2 we negate the number in positon 2 of the list
        if index >= 0 and index < len(nums):
            if nums[index] == 0:
                nums[index] = -inf
            elif nums[index] > 0: 
                nums[index] *= -1

    for index,num in enumerate(nums):
        if num >= 0:
            return index + 1

    return len(nums) + 1