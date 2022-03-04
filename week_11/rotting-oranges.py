# https://leetcode.com/problems/rotting-oranges/submissions/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def anyFresh():
            anyFresh = False
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1:
                        anyFresh = True
            return anyFresh

        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        inBound = lambda r,c : 0<=r<len(grid) and 0<=c<len(grid[0])
        d = {}

        if not anyFresh():
            return 0

        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row,col,0))

        while q:
            curr = q.popleft()
            row, col, level = curr
            if (row,col) not in d:
                d[(row,col)] = level
            else:
                d[(row,col)] = min(d[(row,col)], level)

            for x,y in directions:
                new_row = row + x
                new_col = col + y

                if inBound(new_row,new_col) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((new_row,new_col,level+1))

        if anyFresh():
            return -1

        return max(d.values())
