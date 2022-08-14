# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        matches = defaultdict(list)
        patterns = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                matches[pattern].append(word)
                patterns[word].append(pattern)
                
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        
        while q:
            word, level = q.popleft()
            
            if word == endWord:
                return level
            
            for pattern in patterns[word]:
                for nex in matches[pattern]:
                    if nex not in seen:
                        q.append((nex, level + 1))
                        seen.add(nex)
                        
        return 0
    
