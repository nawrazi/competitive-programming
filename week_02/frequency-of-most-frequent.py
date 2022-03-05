# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        Max = 1
        n = len(nums)-1
        i,j = 0,0

        while j<n:
            diff = nums[i]-nums[j+1]
            if diff<=k:
                j+=1
                Max = max(Max,j-i+1)
                k-=diff

            elif diff>k:
                k+=(nums[i]-nums[i+1])*(j-i)
                i+=1

        return Max
