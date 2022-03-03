# https://leetcode.com/problems/flood-fill/submissions/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def paint(row, col):
            image[row][col] = newColor

            for x, y in directions:
                new_row = row+x
                new_col = col+y

                if in_bound(new_row, new_col) and valid_color(new_row, new_col):
                    paint(new_row, new_col)

        in_bound = lambda r, c : 0 <= r < len(image) and 0 <= c < len(image[0])
        valid_color = lambda r, c : image[r][c] == original

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        original = image[sr][sc]

        if newColor != original:
            paint(sr,sc)

        return image
