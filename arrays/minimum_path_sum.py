
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    # add all numbers on first row together
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    # add all numbers on first column together
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    # since there are just two drns, only the cell above and the cell to the left of each cell
    # can affect the sum of a cell. find the minimum and store in the grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]