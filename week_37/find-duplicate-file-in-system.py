# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)
        for path in paths:
            folder, *files = path.split()
            for file in files:
                name, cont = file.split('(')
                content[cont].append(folder + '/' + name)
                
        return [c for c in content.values() if len(c) > 1]
    
