# https://leetcode.com/problems/create-sorted-array-through-instructions/description/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        costs = [[0, 0] for _ in instructions]
        nums = list(enumerate(instructions))
        
        def merge(start, end):
            if start == end:
                return [nums[start]]
            
            mid = (start + end) // 2
            left = merge(start, mid)
            right = merge(mid + 1, end)
            vals = [l[1] for l in left]
            merged = []
            
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l][1] < right[r][1]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    costs[right[r][0]][0] += l
                    costs[right[r][0]][1] += len(left) - bisect_right(vals, right[r][1])
                    r += 1
                    
            while r < len(right):
                merged.append(right[r])
                costs[right[r][0]][0] += l
                costs[right[r][0]][1] += len(left) - bisect_right(vals, right[r][1])
                r += 1
                
            return merged + left[l:]
        
        mod = pow(10, 9) + 7
        merge(0, len(nums) - 1)
        
        total = 0
        for less, more in costs:
            total += min(less, more) % mod
            
        return total % mod
    
