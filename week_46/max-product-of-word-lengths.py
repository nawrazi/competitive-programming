# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks.append((mask, len(word)))
            
        max_product = 0
        for mask1, length1 in masks:
            for mask2, length2 in masks:
                if mask1 & mask2 == 0:
                    product = length1 * length2
                    max_product = max(max_product, product)
                    
        return max_product
    
