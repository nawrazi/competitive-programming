# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        size = len(p)
        window = Counter(s[:size])
        total = 0
        diff = defaultdict(int)
        for letter, count in window.items():
            diff[letter] = count - p_count.get(letter, 0)
            if diff[letter] != 0:
                total += 1
                
        for letter, count in p_count.items():
            if letter not in diff:
                diff[letter] = -count
                total += 1
                
        anagrams = []
        if total == 0:
            anagrams.append(0)
            
        left, right = 0, size
        while right < len(s):
            if diff[s[left]] == 0:
                total += 1
            diff[s[left]] -= 1
            if diff[s[left]] == 0:
                total -= 1
                
            if diff[s[right]] == 0:
                total += 1
            diff[s[right]] += 1
            if diff[s[right]] == 0:
                total -= 1
                
            left += 1
            right += 1
            
            if total == 0:
                anagrams.append(left)
            
        return anagrams
    
