# https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        m = inf
        after = []
        target = (-1, -1)
        
        for idx, num in enumerate(reversed(arr)):
            after.append((num, len(arr) - idx - 1))
            
            if num > m:
                after.sort()
                for i in range(1, len(after)):
                    if after[i][1] == len(arr) - idx - 1:
                        j = i - 1
                        tar = after[i - 1][0]
                        while j >= 0 and after[j][0] == tar:
                            j -= 1
                        target = (len(arr) - idx - 1, after[j + 1][1])
                        break
                else:
                    continue
                break
            
            m = min(m, num)
            
        if target[0] != -1:
            arr[target[0]], arr[target[1]] = arr[target[1]], arr[target[0]]
            
        return arr
    
