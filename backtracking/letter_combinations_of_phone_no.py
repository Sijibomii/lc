class Solution(object):
    def letterCombinations(self, digits):
    
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    """
    Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
    The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as 
    far as possible along each branch before backtracking.
    """
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            # reached the leave of the tree
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            # consider all branches in the tree
            self.dfs(nums, index+1, dic, path + i, res)