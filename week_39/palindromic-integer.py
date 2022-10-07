# https://binarysearch.com/room/Bytesize-pointers-3sz2jB5VEg?questionsetIndex=0

class Solution:
    def solve(self, num):
        num = str(num)
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
        return True
    
