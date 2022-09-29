# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[i] > q[-1][0]:
                q.pop()
            q.append((nums[i], i - k))
            
        ans = [q[0][0]]
        for i, num in enumerate(nums[k:]):
            while q and num > q[-1][0]:
                q.pop()
            while q and i - q[0][1] >= k:
                q.popleft()
            q.append((num, i))
            ans.append(q[0][0])
            
        return ans
    
