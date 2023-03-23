# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        def findClosest(idx):
            left, right = 0, len(nums) - 1
            best = inf
            
            while left < right:
                if left == idx:
                    left += 1
                    continue
                if right == idx:
                    right -= 1
                    continue
                    
                cur_sum = nums[idx] + nums[left] + nums[right]
                best = min(best, cur_sum, key=lambda x: abs(target - x))
                
                if cur_sum > target:
                    right -= 1
                else:
                    left += 1
                    
            return best
        
        closest = inf
        for idx in range(len(nums)):
            best = findClosest(idx)
            closest = min(closest, best, key=lambda x: abs(target - x))
            
        return closest
    
