# https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        counts = Counter([abs(nums1[i] - nums2[i]) for i in range(len(nums1))])
        
        heap = list(counts.items())
        heap.sort(reverse = True)
        
        moves = k1 + k2
        
        i = 0
        while i < len(heap) and moves > 0:
            diff, count = heap[i]
            
            if i != len(heap) - 1:
                ndiff, ncount= heap[i+1]
            else:
                ndiff, ncount = None, None
            
            if i == len(heap) - 1:
                
                if diff * count <= moves:
                    heap[i] = 0, count
                else:
                    decrements = moves // count
                    leftover = moves % count
                    heap[i] = diff - decrements , count - leftover
                    heap.append((diff - decrements - 1, leftover))         
                    moves = 0
            
            else:
                if (diff - ndiff) * count > moves:
                    decrements = moves // count
                    leftover = moves % count
                    heap[i] = diff - decrements , count - leftover
                    heap.append((diff - decrements - 1, leftover))
                    moves = 0
                
                else:
                    heap[i] = diff , 0
                    heap[i+1] = heap[i+1][0], heap[i+1][1] + count
                    moves -= (diff - ndiff) * count
            
            i += 1
        
        return sum([sum([diff ** 2 for _ in range(count)])  for diff, count in heap])
    
