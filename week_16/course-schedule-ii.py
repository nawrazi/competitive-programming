# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        after, q = defaultdict(set), deque()
        pres = [0] * numCourses
        taken = []

        for course, pre in prerequisites:
            after[pre].add(course)
            pres[course] += 1

        for i, pre in enumerate(pres):
            if pre == 0:
                q.append(i)

        while q:
            course = q.popleft()
            taken.append(course)

            for neighbor in after[course]:
                pres[neighbor] -= 1
                if pres[neighbor] != 0:
                    continue
                q.append(neighbor)

        return taken if len(taken) == numCourses else []
