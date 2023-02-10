# https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        overlaps = Counter()
        
        def getOverlap(sr, sc):
            for row in range(len(img2)):
                for col in range(len(img2)):
                    if img2[row][col] == 1:
                        overlaps[(sr - row, sc - col)] += 1
                        
        for row in range(len(img1)):
            for col in range(len(img1)):
                if img1[row][col] == 1:
                    getOverlap(row, col)
                    
        return max(overlaps.values()) if overlaps else 0
    
