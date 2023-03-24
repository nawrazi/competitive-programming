# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/description/

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        triplets = 0
        
        squares = Counter(pow(num, 2) for num in nums2)
        for idx1, num1 in enumerate(nums1):
            for idx2, num2 in enumerate(nums1):
                if idx1 != idx2:
                    triplets += squares[num1 * num2]
                    
        squares = Counter(pow(num, 2) for num in nums1)
        for idx1, num1 in enumerate(nums2):
            for idx2, num2 in enumerate(nums2):
                if idx1 != idx2:
                    triplets += squares[num1 * num2]
                    
        return triplets // 2
    
