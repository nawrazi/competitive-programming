# https://www.codingninjas.com/codestudio/problems/parallel-courses_1376444

from collections import deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = [set() for _ in range(n + 1)]
    q = deque()
    pres = [0 for _ in range(n + 1)]
    taken = 0
    
    for course, pre in prerequisites:
        graph[pre].add(course)
        pres[course] += 1
        
    q = deque((c, 1) for c in range(1, n + 1) if pres[c] == 0)
    m = 0
    
    while q:
        course, semester = q.popleft()
        m = max(m, semester)
        taken += 1
        
        for neighbor in graph[course]:
            pres[neighbor] -= 1
            if pres[neighbor] == 0:
                q.append((neighbor, semester + 1))
                
    return m if taken == n else -1
