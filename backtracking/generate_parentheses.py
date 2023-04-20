"""
to draw the decision tree you start with 0,0(0 left, 0 right). at first you have to add a left, you can not add a right without left. When you add one left, you have
two decisions, add a corresponding right or add another left. note you can only add a right where left > right. continue like that until no of left equals n
"""
#https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand/
def generateParenthesis(n):
    def dfs(left, right, s):
        if len(s) == n * 2:
            # equal no of right and left
            res.append(s)
            return 

        if left < n:
            # chose to incr left
            dfs(left + 1, right, s + '(')

        if right < left:
            # chose to balance right
            dfs(left, right + 1, s + ')')

    res = []
    dfs(0, 0, '')
    return res