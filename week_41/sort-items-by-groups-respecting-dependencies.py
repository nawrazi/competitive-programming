# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        item_graph = defaultdict(set)
        item_indegrees = []
        group_map = defaultdict(list)
        for i, edges in enumerate(beforeItems):
            if group[i] == -1:
                group[i] = m
                m += 1
            item_indegrees.append(len(edges))
            group_map[group[i]].append(i)
            for e in edges:
                item_graph[e].add(i)
                
        group_graph = defaultdict(set)
        group_indegrees = [set() for _ in range(m)]
        for i, edges in item_graph.items():
            for e in edges:
                if group[i] != group[e]:
                    group_graph[group[i]].add(group[e])
                    group_indegrees[group[e]].add(group[i])
                    
        for i in range(m):
            group_indegrees[i] = len(group_indegrees[i])
            
        def sortGroup(grp):
            sorting = []
            itemq = deque()
            for item in group_map[grp]:
                if item_indegrees[item] == 0:
                    itemq.append(item)
                    
            while itemq:
                item = itemq.popleft()
                sorting.append(item)
                
                for nex in item_graph[item]:
                    item_indegrees[nex] -= 1
                    if item_indegrees[nex] == 0 and group[nex] == grp:
                        itemq.append(nex)
                        
            return sorting
        
        groupq = deque()
        for i, indeg in enumerate(group_indegrees):
            if indeg == 0: 
                groupq.append(i)
                
        top_sort = []
        while groupq:
            grp = groupq.popleft()
            top_sort += sortGroup(grp)
            
            for nex_grp in group_graph[grp]:
                group_indegrees[nex_grp] -= 1
                if group_indegrees[nex_grp] == 0:
                    groupq.append(nex_grp)
                    
        return top_sort if len(top_sort) == n else []
    
