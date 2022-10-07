# https://binarysearch.com/room/Bytesize-pointers-3sz2jB5VEg?questionsetIndex=1

class Solution:
    def solve(self, n, x, y, k):
        directions = [(2,1), (1,2), (-1,2), (2,-1), (-1,-2), (-2,-1), (1,-2), (-2,1)]
        inBound = lambda r, c: 0 <= r < n and 0 <= c < n
        
        @cache
        def dfs(row, col, lev):
            if lev == k:
                return 1

            ways = 0
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c):
                    continue
                ways += dfs(r, c, lev + 1)

            return ways

        return floor((dfs(x, y, 0) / (8 ** k)) * 100)
    
