# https://leetcode.com/problems/reorder-data-in-log-files/description/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        
        for log in logs:
            identifier, *content = log.split()
            if content[0].isnumeric():
                digit.append(log)
            else:
                letter.append([' '.join(content), identifier])
                
        return [' '.join(log[::-1]) for log in sorted(letter)] + digit
    
