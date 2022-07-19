# https://leetcode.com/problems/subarray-sum-equals-k/
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/2301103/Python-HashMap-O(n)-(Explanation)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        count, cur_sum = 0, 0
        for num in nums:
            seen[cur_sum] += 1
            cur_sum += num
            count += seen[cur_sum - k]
            
        return count
    
