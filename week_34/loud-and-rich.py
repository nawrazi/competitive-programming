# https://leetcode.com/problems/loud-and-rich/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        @cache
        def getQuietest(node):
            quietest = (node, quiet[node])
            for nex in graph[node]:
                nex_node, nex_quiet = getQuietest(nex)
                if nex_quiet < quietest[1]:
                    quietest = (nex_node, nex_quiet)
                
            return quietest
        
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        
        return [getQuietest(i)[0] for i in range(len(quiet))]
    
