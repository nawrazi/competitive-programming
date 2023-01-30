# https://leetcode.com/problems/alphabet-board-path/description/

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def path(start, end):
            if start == 'z':
                return 'U' + path('u', end) if end != 'z' else ''
            
            if end == 'z':
                return path(start, 'u') + 'D'
            
            direction = [{-1: 'L', 1: 'R'}, {-1: 'U', 1: 'D'}]
            value = lambda char: ord(char) - ord('a')
            
            horizontal = (value(end) % 5) - (value(start) % 5)
            vertical = (value(end) // 5) - (value(start) // 5)
            
            def motion(axis, distance):
                if distance == 0:
                    return ''
                return abs(distance) * direction[axis][distance // abs(distance)]
            
            return motion(0, horizontal) + motion(1, vertical)
        
        sequence = []
        target = 'a' + target
        for i in range(1, len(target)):
            sequence.append(path(target[i - 1], target[i]))
            
        return '!'.join(sequence) + '!'
    
