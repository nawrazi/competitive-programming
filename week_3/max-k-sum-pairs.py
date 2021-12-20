# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, counter = 0, len(nums)-1, 0
        while i<j:
            if nums[i]+nums[j] < k:
                i+=1
            elif nums[i]+nums[j] > k:
                j-=1
            else:
                counter+=1
                i+=1
                j-=1

        return counter
