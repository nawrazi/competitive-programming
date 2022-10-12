# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and -asteroid > stack[-1]:
                    stack.pop()
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
                    
        return stack
    
