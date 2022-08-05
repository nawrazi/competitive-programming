# https://leetcode.com/problems/describe-the-painting/

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        borders = set()
        size = 0
        for start, end, _ in segments:
            size = max(size, max(start, end))
            borders.add(end)
            
        painting = [0 for _ in range(size + 1)]
        
        for start, end, color in segments:
            painting[start] += color
            painting[end] -= color
            
        color = 0
        for i in range(len(painting)):
            fir = color
            color += painting[i]
            painting[i] = fir
            
        ans = []
        cur = painting[0]
        s = 0
        for e in range(size + 1):
            if painting[e] != cur or e - 1 in borders:
                if cur != 0:
                    ans.append([s - 1, e - 1, cur])
                cur = painting[e]
                s = e
                
        ans.append([s - 1, e, cur])
        return ans
    
