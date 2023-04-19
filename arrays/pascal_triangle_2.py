# check soln_1 to understand more
def pascal_triangle(rowIndex):
    res = [[1]]
    # rowIndex+1 bc they didn't count the row containing just [1]
    for i in range(1, rowIndex+1):
        #The map() function executes a specified function for each item in an iterable. the func in this cal takes in x, y
        res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    return res[-1]


# soln 2
def get_factorial(self, n):
    if self.rowIndex == n and hasattr(self, 'fact_n') and self.fact_n is not None:
        return self.fact_n
    else:
        fact = 1
        for i in range(n):
            fact *= (i+1)
        return fact
# entry point
def getRow(self, rowIndex: int):
    """
    as binomial theorom nth row constants will be >> [nC0, nC1, nC2, .... nCn] { n+1 items [0, n]} where  nCr= n! / ( r! * (n-r)!)
    """
    self.rowIndex = rowIndex
    self.fact_n = self.get_factorial(rowIndex)
    

    res = []
    for i in range((rowIndex)//2 +1):
        denomi = self.get_factorial(i) * self.get_factorial(rowIndex-i)
        res.append(int(self.fact_n/denomi))
    
    if rowIndex%2 != 0:
        return res + res[::-1]
    else:
        return res + res[::-1][1:]