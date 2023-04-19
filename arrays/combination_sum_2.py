
def combination(nums, target, path, ret):
    if target < 0:
        return 
    if target == 0 and ret.count(path) == 0:
        ret.append(path)
        return 
    for i in range(len(nums)):
        combination(nums[i+1:], target-nums[i], path+[nums[i]], ret)


def combination_sum_2(candidates, target): 
    ret = []
    combination(sorted(candidates), target, [], ret)
    return ret

print(combination_sum_2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))


################################################################################################################################################

def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    def dfs(idx, path, cur):
        if cur > target: return
        if cur == target:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                # this ensures it does not repeat path. if i > idx and candidates[i] == candidates[i-1] then that path has been checked
                continue
            dfs(i+1, path+[candidates[i]], cur+candidates[i])
    dfs(0, [], 0)
    return res

