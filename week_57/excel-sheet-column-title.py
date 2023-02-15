# https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber > 0:
            if columnNumber % 26 == 0:
                title.append('Z')
                columnNumber = (columnNumber // 26) - 1
            else:
                title.append(chr(ord('A') + (columnNumber % 26) - 1))
                columnNumber //= 26
                
        return ''.join(reversed(title))
    
