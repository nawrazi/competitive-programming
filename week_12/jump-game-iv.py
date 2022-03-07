# https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = {}

        for i, num in enumerate(arr):
            if num in d:
                heapq.heappush(d[num], (len(arr) - i, i))
            else:
                d[num] = [(len(arr) - i, i)]

        q = deque([(0, 0)])
        seen = set([0])

        while q:
            curr, level = q.popleft()

            if curr == len(arr) - 1:
                return level

            while d[arr[curr]]:
                _, index = heapq.heappop(d[arr[curr]])
                if 0 <= index < len(arr) and index not in seen:
                    seen.add(index)
                    q.append((index, level+1))

            for index in (curr + 1, curr - 1):
                if 0 <= index < len(arr) and index not in seen:
                    seen.add(index)
                    q.append((index, level+1))
