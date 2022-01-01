# https://leetcode.com/problems/find-original-array-from-doubled-array/submissions/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original, references, ans = [], {}, []

        if set(changed)=={0} and len(changed)%2==0:
            return [0]*(len(changed)//2)

        for num in changed:
            if num%2==0 and num//2 in references:
                if references[num//2]==0:
                    if num in references:
                        references[num]+=1
                    else:
                        references[num]=1
                else:
                    references[num//2]-=1
                    ans.append(num//2)

            else:
                if num in references:
                    references[num]+=1
                else:
                    references[num] = 1

        return ans if set(references.values())=={0} else []
