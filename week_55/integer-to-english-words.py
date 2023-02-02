# https://leetcode.com/problems/integer-to-english-words/description/

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = {
            '0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
            '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
        }
        tens = {
            '0': '', '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty',
            '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'
        }
        teen = {
            '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
            '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'
        }
        place = {
            1: 'Thousand', 2: 'Million', 3: 'Billion'
        }
        
        def toWord(num, power):
            word = []
            
            if num[0] != '0':
                word.append(ones[num[0]])
                word.append('Hundred')
                
            if num[1] == '1':
                word.append(teen[num[1:]])
            else:
                word.append(tens[num[1]])
                word.append(ones[num[2]])
                
            if power > 0 and num != '000':
                word.append(place[power])
                
            return ' '.join(w for w in word if w)
        
        if num == 0:
            return 'Zero'
        
        num = ('0' * (3 - (len(str(num)) % 3))) + str(num)
        word = []
        power = (len(num) // 3) - 1
        
        for idx in range(0, len(num), 3):
            word.append(toWord(num[idx:idx+3], power))
            power -= 1
            
        return ' '.join(w for w in word if w)
    
