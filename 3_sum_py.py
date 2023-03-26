# 1. brute force approach

"""
2
"""
def three_sum(nums):
    res = set()

    #1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0: 
            n.append(num)
        else:
            z.append(num)

    #2. Create a separate set for negatives and positives for O(1) look-up times
    N, P = set(n), set(p) 

    #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                res.add(tuple(sorted([p[i],p[j],target])))

    return res


"""
3. sort first 
""" 
# NOTE ANSWER IS PARTIALLY CORRECT BUT DUPLICATE LOGIC BELOW IS WRONG
def three_sum(nums):
    nums = sorted(nums)
    # TURN THIS INTO A SET
    answer = []
    for idx, num in enumerate(nums):
        low = idx + 1
        high = len(nums) - 1
        while low < high:
            if num + nums[low] + nums[high] < 0:
                #increment low to find an higher number so total can move closer to 0
                low = low + 1
            elif num + nums[low] + nums[high] > 0:
                #increment hight to find a lower number so the total can move closer to 0
                high = high - 1
            else:
                # a match has been found i.e total = 0
                answer.append([num, nums[low], nums[high]])
                # logic below is meant to eliminate duplicates to save time
                temp1 = low
                temp2 = high
                while (low < high) and (nums[low] == nums[temp1]):
                    #[-1, 0,1,1,1,3,4,5] assuming low was at index 2, we skip new low to index 5 since others are duplicates
                    low= low + 1
                while (low < high) and (nums[high] == nums[temp2]):
                    #same logic but for high
                    high = high - 1
        # same here, eliminate duplicates on num
        # logic to prevent duplicate is wrong
       
        # while (idx + 1 < len(nums)) and (nums[idx] == nums[idx+1]):
            
    return answer
 