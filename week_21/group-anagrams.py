# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts = [''.join(sorted(s)) for s in strs]
        anagrams = defaultdict(list)
        
        for i, s in enumerate(sorts):
            anagrams[s].append(strs[i])
            
        return anagrams.values()
