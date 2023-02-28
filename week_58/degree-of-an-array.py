# https://leetcode.com/problems/degree-of-an-array/description/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def degree(counter):
            if not counter:
                return 0
            return max(counter.values())
        
        left = 0
        counter = Counter()
        target = degree(Counter(nums))
        min_length = inf
        nums.append(-1)
        
        for right in range(len(nums)):
            while degree(counter) >= target:
                min_length = min(min_length, right - left)
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
                
            counter[nums[right]] += 1
            
        return min_length
    
