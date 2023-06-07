# https://leetcode.com/problems/interval-list-intersections/description/

class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        idx1, idx2 = 0, 0
        inters = []
        
        while idx1 < len(first) and idx2 < len(second):
            start, end = max(first[idx1][0], second[idx2][0]), min(first[idx1][1], second[idx2][1])
            if start <= end:
                inters.append([start, end])
            if first[idx1][1] < second[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        
        return inters
    
