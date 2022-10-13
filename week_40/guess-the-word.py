# https://leetcode.com/problems/guess-the-word/

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        graph = {word: [set() for _ in range(6)] for word in words}
        
        for word1 in words:
            for word2 in words:
                matches = 6
                for i in range(6):
                    if word1[i] != word2[i]:
                        matches -= 1
                        
                if matches < 6:
                    graph[word1][matches].add(word2)
                    graph[word2][matches].add(word1)
                    
        pool = set(words)
        q = deque([words[0]])
        seen = {words[0]}
        
        while q:
            word = q.popleft()
            matches = master.guess(word)
            
            if matches == 6:
                break
                
            for w in words:
                if w not in graph[word][matches]:
                    pool.discard(w)
                    
            if len(pool) == 1:
                master.guess(list(pool)[0])
                break
                
            for nex in pool:
                if nex not in seen:
                    q.append(nex)
                    seen.add(nex)
                    
