# https://leetcode.com/problems/largest-values-from-labels/

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        groups = defaultdict(list)
        for i in range(len(values)):
            heappush(groups[labels[i]], -values[i])
            
        chosen = []
        for group in groups.values():
            for _ in range(useLimit):
                if group:
                    chosen.append(-heappop(group))
                else:
                    break
                    
        chosen.sort(reverse = True)
        return sum(chosen[:numWanted])
    
