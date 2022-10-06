# https://binarysearch.com/room/How-do-I-Java-CK7pAOMFwT

class Solution:
    def solve(self, relations):
        foll = defaultdict(set)
        ans = set()
        for x, y in relations:
            if x in foll[y]:
                ans.add(x)
                ans.add(y)
            foll[x].add(y)
        return sorted(list(ans))
    
