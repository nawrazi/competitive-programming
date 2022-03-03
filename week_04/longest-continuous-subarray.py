# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxx, min_queue, max_queue = 1, deque(), deque()
        n = len(nums)
        l, r = 0, 0
        while r<n:
            num = nums[r]

            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)

            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)

            while l<=r and abs(max_queue[0] - min_queue[0]) > limit:
                if nums[l] == max_queue[0]:
                    max_queue.popleft()
                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                l+=1

            maxx = max(maxx, r-l+1)
            r+=1

        return maxx
