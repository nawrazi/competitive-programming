# https://leetcode.com/problems/integer-to-english-words/description/

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teen = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        place = ['', 'Thousand', 'Million', 'Billion']
        
        def convert(num, power):
            words = []
            
            if num[0] != '0':
                words.append(ones[int(num[0])])
                words.append('Hundred')
                
            if num[1] == '1':
                words.append(teen[int(num[1:]) - 10])
            else:
                words.append(tens[int(num[1])])
                words.append(ones[int(num[2])])
                
            if int(num) != 0:
                words.append(place[power])
                
            return ' '.join(w for w in words if w)
        
        if num == 0:
            return 'Zero'
        
        num = ('0' * (3 - (len(str(num)) % 3))) + str(num)
        power = (len(num) // 3) - 1
        words = []
        
        for idx in range(0, len(num), 3):
            words.append(convert(num[idx:idx+3], power))
            power -= 1
            
        return ' '.join(w for w in words if w)
    
