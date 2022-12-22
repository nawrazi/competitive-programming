# https://leetcode.com/problems/cycle-length-queries-in-a-tree/

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        for node1, node2 in queries:
            cycle = 0
            path = set()
            
            while node1 != 0:
                cycle += 1
                path.add(node1)
                node1 //= 2
                
            while node2 != 0:
                if node2 in path:
                    cycle -= 1
                else:
                    cycle += 1
                node2 //= 2
                
            yield cycle + 1
        
