# https://leetcode.com/problems/integer-to-english-words/description/

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teen = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        place = ['', 'Thousand', 'Million', 'Billion']
        
        def toWord(num, power):
            word = []
            
            if num[0] != '0':
                word.append(ones[int(num[0])])
                word.append('Hundred')
                
            if num[1] == '1':
                word.append(teen[int(num[1:]) - 10])
            else:
                word.append(tens[int(num[1])])
                word.append(ones[int(num[2])])
                
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
    
