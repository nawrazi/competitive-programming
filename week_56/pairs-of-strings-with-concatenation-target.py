# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/description/

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    pairs += 1
                    
        return pairs
    
