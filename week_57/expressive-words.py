# https://leetcode.com/problems/expressive-words/description/

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def summarize(word):
            summary = []
            last = [word[0], 0]
            for c in word + ' ':
                if c != last[0]:
                    summary.append(tuple(last))
                    last = [c, 1]
                else:
                    last[1] += 1
                    
            return summary
        
        stretched = summarize(s)
        stretchy = 0
        for word in words:
            summary = summarize(word)
            if len(summary) != len(stretched):
                continue
                
            for (chr1, cnt1), (chr2, cnt2) in zip(stretched, summary):
                if chr1 != chr2 or cnt2 > cnt1:
                    break
                if cnt1 != cnt2 and cnt1 < 3:
                    break
            else:
                stretchy += 1
                
        return stretchy
    
