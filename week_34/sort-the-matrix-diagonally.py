# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def search(row, col, place, idx):
            if not inBound(row, col):
                return
            
            if place:
                ans[row][col] = current[idx]
                search(row + 1, col + 1, place, idx + 1)
            else:
                current.append(mat[row][col])
                search(row + 1, col + 1, place, idx)
                
        ans = [[0 for _ in range(n)] for _ in range(m)]
        starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(1, m)]
        
        for r, c in starts:
            current = []
            search(r, c, False, 0)
            current.sort()
            search(r, c, True, 0)
            
        return ans
    
