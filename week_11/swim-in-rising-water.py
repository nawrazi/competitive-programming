# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        inBound = lambda r,c : 0<=r<len(grid) and 0<=c<len(grid[0])
        seen = set()
        heap = [(grid[0][0], 0, 0)]
        max_height = 0

        while heap:
            height, row, col = heappop(heap)
            max_height = max(height, max_height)
            seen.add((row,col))

            if grid[row][col] == grid[-1][-1]:
                break

            for x,y in directions:
                new_row = row + x
                new_col = col + y

                if inBound(new_row,new_col) and (new_row,new_col) not in seen:
                    heappush(heap, (grid[new_row][new_col],new_row,new_col))

        return max_height
