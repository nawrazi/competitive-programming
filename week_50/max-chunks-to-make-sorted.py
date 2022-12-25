# https://leetcode.com/problems/max-chunks-to-make-sorted/description/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        expected = {0}
        
        for border in range(1, len(arr) + 1):
            for num in arr[:border]:
                if num not in expected:
                    break
            else:
                chunks += 1
            expected.add(border)
            
        return chunks
    
