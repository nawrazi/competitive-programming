# https://www.hackerrank.com/contests/a2sv-3-contest-4/challenges/tree-height-of-a-binary-tree

def height(root):
    if root is None:
        return -1

    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)

    return max(left_height, right_height)
