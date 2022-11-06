# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

def checkRows(grid, topRow):
    n = len(grid[topRow])
    same = grid[topRow][0] == grid[topRow + 1][0]
    
    for col in range(1, n):
        if same and grid[topRow][col] != grid[topRow + 1][col]:
            return False
        if not same and grid[topRow][col] == grid[topRow + 1][col]:
            return False
        
    return True

def isPossible(grid):
    m = len(grid)
    
    for row in range(m - 1):
        validRows = checkRows(grid, row)
        if not validRows:
            return False
        
    return True
