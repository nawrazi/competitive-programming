# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = (10 ** 9) + 7
        dp = []
        prev = {
            'a': {'i', 'u', 'e'},
            'e': {'i', 'a'},
            'i': {'o', 'e'},
            'o': {'i'},
            'u': {'i', 'o'}
        }
        
        for v in prev.keys():
            dp.append([0 for _ in range(n)])
            dp[-1][-1] = 1
            nex = {v: 1}
            for i in range(n - 2, -1, -1):
                cur = defaultdict(int)
                for c, m in nex.items():
                    for p in prev[c]:
                        cur[p] += m % mod
                        dp[-1][i] += m % mod
                nex = cur
                
        return sum(d[0] for d in dp) % mod
    
