class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        # Input: candidates = [10,1,2,7,6,1,5], target = 8
        def backtracking(curr, pos, target):
            if target == 0:
                # make a copy bc the curr will also be passed around to other iterations so it does not get modified
                res.append(curr.copy())
                return
            
            if target < 0:
                return 
            prev = -1

            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    # arr is in sorted order so if candidates[i] == prev it means we've checked a path with that number
                    continue
                curr.append(candidates[i])
                backtracking(curr, i+1, target-candidates[i])
                # this happens after a match has been found ot target < 0. i.e there has been a return
                # curr.pop() removes the latest or last candidate to be added to path curr
                curr.pop()
                # this makes sure on other iterations of the for loop no path with candidate[i] is considered
                prev = candidates[i]
        backtracking([], 0, target)
        return res

       


