# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words.append(' ' * maxWidth)
        lines = []
        spaces = {}
        
        line = []
        length = 0
        for word in words:
            if len(word) + length > maxWidth:
                spaces[len(lines)] = maxWidth - (length - 1)
                lines.append(line[:])
                line = [word]
                length = len(word) + 1
            else:
                line.append(word)
                length += len(word) + 1
        
        text = []
        for i in range(len(lines) - 1):
            line = lines[i]
            gaps = len(line) - 1
            equal = spaces[i] // gaps if gaps else spaces[i]
            left = spaces[i] % gaps if gaps else 0
            
            cur = []
            for word in line[:-1]:
                space = ' ' * equal
                if left > 0:
                    space += ' '
                    left -= 1
                cur.append(word + space)
            
            if len(line) == 1:
                cur.append(line[-1] + ' ' * spaces[i])
            else:
                cur.append(line[-1])
                
            text.append(' '.join(cur))
                
        text.append(' '.join(lines[-1]) + (' ' * spaces[len(lines) - 1]))
        
        return text
    
