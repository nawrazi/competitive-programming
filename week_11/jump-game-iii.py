# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        inBound = lambda idx : 0<=idx<len(arr)
        seen = set()

        while q:
            curr = q.popleft()
            seen.add(curr)

            if arr[curr] == 0:
                return True

            left = curr - arr[curr]
            right = curr + arr[curr]
            directions = [left, right]

            for index in directions:
                if inBound(index) and index not in seen:
                    q.append(index)

        return False
