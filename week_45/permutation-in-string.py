# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2 += ' '
        perm = Counter(s1)
        size = len(s1)
        diff = defaultdict(int)
        total = 0
        
        for letter, count in Counter(s2[:size]).items():
            diff[letter] = count - perm[letter]
            if diff[letter] != 0:
                total += 1
                
        for letter, count in perm.items():
            if letter not in diff:
                diff[letter] = -count
                total += 1
                
        left, right = 0, size
        while right < len(s2):
            if total == 0:
                return True
            
            if diff[s2[left]] == 0:
                total += 1
            diff[s2[left]] -= 1
            if diff[s2[left]] == 0:
                total -= 1
                
            if diff[s2[right]] == 0:
                total += 1
            diff[s2[right]] += 1
            if diff[s2[right]] == 0:
                total -= 1
                
            left += 1
            right += 1
            
        return False
    
