# https://leetcode.com/problems/count-collisions-on-a-road/description/

class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        
        for car in directions:
            if car == 'L':
                if stack and stack[-1] == 'S':
                    stack[-1] = 'S'
                    collisions += 1
                    continue
                    
                if not stack or stack[-1] != 'R':
                    continue
                    
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                    
                collisions += 1
                stack.append('S')
                
            elif car == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append('S')
                
            else:
                stack.append('R')
                
        return collisions
    
