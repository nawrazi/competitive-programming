# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        after, q = defaultdict(set), deque()
        pres = [0] * numCourses
        taken = 0

        for course, pre in prerequisites:
            after[pre].add(course)
            pres[course] += 1

        for i, pre in enumerate(pres):
            if pre == 0:
                q.append(i)
                
        while q:
            course = q.popleft()
            taken += 1
            for neighbor in after[course]:
                pres[neighbor] -= 1
                if pres[neighbor] != 0:
                    continue
                q.append(neighbor)

        return taken == numCourses
