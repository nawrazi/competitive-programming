class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([(root,0)])
        averages = []

        while q:
            curr, level = q.popleft()
            if level<len(averages):
                averages[level][0]+=curr.val
                averages[level][1]+=1
            else:
                averages.append([curr.val,1])

            if curr.left:
                q.append((curr.left,level+1))
            if curr.right:
                q.append((curr.right,level+1))

        return [s/n for s,n in averages]
