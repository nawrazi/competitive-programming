# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = defaultdict(int)
        dna = list(s)

        i, j = 0, 9
        while j < len(s):
            seq = ''.join(dna[i:j+1])
            freq[seq] += 1
            i += 1
            j += 1

        return filter(lambda seq : freq[seq] > 1, freq.keys())
