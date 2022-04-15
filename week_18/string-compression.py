# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(chars[-1])
        cur = chars[0]
        length = 0
        compressed = []

        for i, char in enumerate(chars):
            if char != cur or i == len(chars) - 1:
                compressed.append(cur)
                if length > 1:
                    compressed += list(str(length))
                length = 0
                
            cur = char
            length += 1

        chars[:] = compressed
