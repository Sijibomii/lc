# https://www.youtube.com/watch?v=HAA8mgxlov8
class Solution:
    def isMatch(self, s, p):

        cache = {}

        # i is the index for the string, j is the index for the pattern
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                #string has been successfully matched
                return True
            
            if j >= len(p):
                # pattern is out of bounds and i is not out of bounds 
                # i.e there is some string in s still unmatched
                return False
            
            is_match = (i < len(s) and ( # check if i is not out of bound
                s[i] == p[j] #the char in the two idx are they equal?
                or
                p[j] == "." # period matches any character
            ))
            # we do not check this in the beginning bc we know that * can not be at the beginnning of a pattern
            if (j+1) < len(p) and p[j+1] == "*":
                #if there is a star in the next idx in the pattern note that * is for repeating. we also check to see if there is a j+1

                # when we have a "*" we have two choices:
                # 1. don't use the star i.e do not repeat the prev char

                #2. use the star. i.e repeat the char. if we are using the star note that we can only use the star for the next char in the string if there was a 
                # match in the current one

                # if any returns true, we can return true(store in cache)
                cache[(i, j)] = dfs(i, j+2) or (is_match and dfs(i+1, j))
                return cache[(i, j)]
                
            
            if is_match:
                # there was a char to char match
                cache[(i, j)]= dfs(i+1, j+1)
                return cache[(i, j)]

            # no match
            cache[(i, j)] = False
            return False
        return dfs(0,0)
        
                

            
            