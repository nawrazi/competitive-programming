# https://leetcode.com/problems/match-substring-after-replacement/description/

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        equiv = defaultdict(set)
        for old, new in mappings:
            equiv[old].add(new)
            
        for idx in range(len(s) - len(sub) + 1):
            for char in sub:
                if s[idx] != char and s[idx] not in equiv[char]:
                    break
                idx += 1
            else:
                return True
            
