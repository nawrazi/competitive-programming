# https://binarysearch.com/room/How-do-I-Java-CK7pAOMFwT?questionsetIndex=2

class Solution:
    def solve(self, matrix):
        m, n = len(matrix), len(matrix[0])
        def color():
            q = deque([(0, 0)])
            seen = {(0, 0)}
            cur = matrix[0][0]
            total = 0
            while q:
                row, col = q.popleft()
                matrix[row][col] = 1 - cur
                total += 1

                for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                    r, c = row + x, col + y
                    if (r, c) not in seen and 0 <= r < m and 0 <= c < n:
                        if matrix[r][c] == cur:
                            q.append((r, c))
                            seen.add((r, c))

            return total == m * n

        ops = 0
        while True:
            if color():
                return ops
            ops += 1
            
