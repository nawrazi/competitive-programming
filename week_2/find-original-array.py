# INCOMPLETE

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        n = len(changed)
        original = []

        for num in changed:
            j=1
            while j<n:
                if changed[j]%2==0 and changed[j]//2==changed[0]:
                    original.append(changed.pop(0))
                    changed.pop(j-1)
                    n-=2
                    j=1
                else:
                    j+=1

        return original if len(changed) == 0 else []
