# [1,2,3]
def subsets(nums):
    ret = []
    dfs(nums, [], ret)
    return ret

# dfs method
def dfs(nums, path, ret):
    ret.append(path)
    for i in range(len(nums)):
        dfs(nums[i+1:], path+[nums[i]], ret)