# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diags = defaultdict(list)
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                diags[r - c].append(cell)
        
        for diag in diags.values():
            diag.sort(reverse = True)
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                ans[r][c] = diags[r - c].pop()
                
        return ans
    
