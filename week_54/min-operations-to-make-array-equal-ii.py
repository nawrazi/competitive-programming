# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/description/

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if nums1 == nums2:
            return 0
        
        diff = 0
        total = 0
        for a, b in zip(nums1, nums2):
            if k == 0 or abs(a - b) % k != 0:
                return -1
            if a > b:
                diff += abs(a - b)
            else:
                diff -= abs(a - b)
            total += abs(a - b)
        
        return total // (2 * k) if diff == 0 else -1
    
