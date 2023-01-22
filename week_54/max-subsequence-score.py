# https://leetcode.com/problems/maximum-subsequence-score/description/

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = sorted(map(tuple, zip(nums2, nums1)))
        
        cur_sum = 0
        heap = []
        for i in range(k):
            cur_sum += pairs[~i][1]
            heappush(heap, pairs[~i][1])
        
        max_score = cur_sum * pairs[n - k][0]
        for idx in range(n - k - 1, -1, -1):
            if pairs[idx][1] > heap[0]:
                cur_sum += pairs[idx][1] - heappop(heap)
                heappush(heap, pairs[idx][1])
                score = cur_sum * pairs[idx][0]
                max_score = max(max_score, score)
        
        return max_score
    
