# https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pres = defaultdict(set)

        for pre, course in prerequisites:
            pres[course].add(pre)
            pres[course].update(pres[pre])

        for i in range(len(prerequisites) - 1, -1, -1):
            pre, course = prerequisites[i]
            pres[course].add(pre)
            pres[course].update(pres[pre])

        return [pre in pres[course] for pre, course in queries]
