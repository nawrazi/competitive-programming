# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        pres = [0] * n

        for start, end in edges:
            graph[start].append(end)
            pres[end] += 1

        q = deque(filter(lambda i: pres[i] == 0, range(n)))
        ancestors = [set() for _ in range(n)]

        while q:
            node = q.popleft()

            for nex in graph[node]:
                ancestors[nex].add(node)
                ancestors[nex].update(ancestors[node])
                pres[nex] -= 1
                if pres[nex] == 0:
                    q.append(nex)

        return [sorted(list(ancestor)) for ancestor in ancestors]
