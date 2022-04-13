# https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        @lru_cache(None)
        def getTime(course):
            if not graph[course]:
                return time[course - 1]

            max_time = float(-inf)
            for crs in graph[course]:
                max_time = max(getTime(crs), max_time)

            return time[course - 1] + max_time

        graph = defaultdict(list)

        for i, (pre, course) in enumerate(relations):
            graph[course].append(pre)

        graph[n + 1] = [i + 1 for i in range(n)]
        time.append(0)

        return getTime(n + 1)
